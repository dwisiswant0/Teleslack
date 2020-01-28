#!/usr/bin/env python3

import os
import sys
import yaml
from Teleslack import Teleslack

cfg 	  = yaml.load(open("config.yaml", "r"))
teleslack = Teleslack(cfg['telegram']['name'], cfg['telegram']['api_id'], cfg['telegram']['api_hash'])
messages  = teleslack.parsingMessages(cfg['telegram']['channels'])
log_file  = os.path.join(os.path.abspath(cfg['slack']['log']))

for channel, message in messages.items():
	for i in message:
		if i.fwd_from is None:
			pattern = "%s.%d" % (channel, i.id)
			check	= teleslack.Logger(log_file, pattern)
			print("#### " + pattern)
			if check:
				print("Already posted. SKIPPING!")
			else:
				print("Post to Slack...")
				posting = teleslack.doPosting(cfg['slack']['webhook'], i.message, log_file)
				if posting:
					print("OK!");
					write = teleslack.Logger(log_file, pattern, True)
				else:
					print("FAILED")