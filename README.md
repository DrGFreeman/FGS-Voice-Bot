# FGS-Voice-Bot
Flat Galaxy Society Discord bot to assign a role to users active in voice channels and remove the role when they leave voice channels.


## Bot Configuration

The bot configuration must be defined in a file named `.env` with the following format:

```
ROLE_ID = 312345678012345678
TOKEN = <bot_token>
```

Where `ROLE_ID` is the id of the role to be assigned to players active in a voice channel and `TOKEN` is the bot token. The role id can be obtained with the `\@Role_Name` command in any channel of the server.

## Usage

### Docker

The repository includes a docker file to run the application in a Docker container. Build and run the container with the following commands:

```
docker build -t fgs_voice_bot .
docker run --rm -d fgs_voice_bot
```

### Python Virtual Environment

Alternatively the application can be run in a Python virtual environment. First create a virtual environment:

```
python3.10 -m venv .venv --prompt=fgs-voice-bot
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Then run the application:

```
python fgs_voice_bot.py
```