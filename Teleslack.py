import os
import sys
import json
import requests
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import GetHistoryRequest

class Teleslack:
	def __init__(self, name, api_id, api_hash):
		self.name = name
		self.api_id = api_id
		self.api_hash = api_hash

	def getMessages(self, channel_username):
		with TelegramClient(self.name, self.api_id, self.api_hash) as client:
			channel_entity = client.get_input_entity(channel_username)
			messages 	   = client(
				GetHistoryRequest(
					peer=channel_entity,
					limit=10,
					offset_date=None,
					offset_id=0,
					max_id=0,
					min_id=0,
					add_offset=0,
					hash=0
				)
			)
			return channel_username, messages
		
	def parsingMessages(self, channel_collections):
		messages = {}
		for channel in channel_collections:
			from_channel, posts = self.getMessages(channel)
			messages[from_channel] = posts.messages

		return messages

	def Logger(self, file, pattern, save=False):
		if os.path.exists(file):
			mode = "a" if save else "r"
		else:
			os.makedirs(file)
		with open(str(file), mode) as log:
			if save:
				log.write("%s\r\n" % (pattern))
			else:
				if pattern in log.read():
					return True
				else:
					return False

	def doPosting(self, webhook, text, log_file):
		response = requests.post(
			webhook, data=json.dumps({"text": text}),
			headers={"Content-Type": "application/json"}
		)

		if response.status_code != 200:
			return False
			# raise ValueError(
			# 	'Request to Slack returned an error %s, the response is:\n%s'
			# 	% (response.status_code, response.text)
			# )

		return True