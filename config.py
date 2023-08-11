# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "11677823"))
API_HASH = os.environ.get("API_HASH", "f1be9e535abfe6f3e75d0acaa6925bc1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5843088812:AAF10GRUY6rcQpPDeVcMqOqs2y7FL5v3Q-E")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1905927769")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "snapurl")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://snapurl:snapurl@snap.cpt24qs.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1905927769")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1905927769)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001916048501")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "STATUSLOVER30") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "false") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://snapurl.me/img/member-area-logo.png') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
