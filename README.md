## Teleslack

### Installation

#### Dependencies

```bash
$ pip3 install -U telethon --user
```

#### Setup

```bash
$ git clone git@github.com:dwisiswant0/Teleslack.git
$ cd Teleslack
$ cp config.yaml.sample config.yaml
```

### Configuration

```yaml
telegram:
  name    : "dw1" # session name
  api_id  : **********
  api_hash: "**********"
  ## Public Telegram Channels ##
  channels:
    - "thehackernews"
    - "thebugbountyhunter"

slack:
  webhook: "https://hooks.slack.com/services/**********" # Incoming Webhooks URL
  log    : "channel-messages.log" # Log file
```

#### Telegram

1. [Login to your Telegram account](https://my.telegram.org/) with the phone number of the developer account to use.
2. Click under API Development tools.
3. A _**Create new application**_ window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
4. Click on Create application at the end. Remember that your **API hash is secret** and Telegram won’t let you revoke it. Don’t post it anywhere!

> This API ID and hash is the one used by your application, not your phone number. You can use this API ID and hash with any phone number or even for bot accounts.

#### Slack

Read this [basic app Slack setup](https://api.slack.com/authentication/basics).

### Usage

Cron every 30 minutes _(recommended)_.

```bash
*/30 * * * * cd /home/dw1/Teleslack && /usr/bin/python3 main.py
```