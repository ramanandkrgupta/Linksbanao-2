# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "11677823"))
API_HASH = os.environ.get("API_HASH", "f1be9e535abfe6f3e75d0acaa6925bc1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5864588864:AAGLEEY8cQSL7MwFu-PP3O_V7w9K7nMK7LU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1905927769")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "linksbanao")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://linksbanao:os6ZPnJ1jw8ktsNB@linksbanao.9rapmnc.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1905927769")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1905927769)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001976950989")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "linksbanao_site") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "True"
IS_PRIVATE = is_enabled(
    os.environ.get("IS_PRIVATE", "False"), "False"
)  # true for private use and restricting users
