# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
      
# Owner Information
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
ADMINS = int(environ.get("ADMINS", ""))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://cloneeternalbot:6YLRrjgIkf4fU2kZ@cluster0.kiebnh6.mongodb.net/?retryWrites=true&w=majority")
CDB_NAME = environ.get("CDB_NAME", "cloneeternalbot")
DB_URI = environ.get("DB_URI", "mongodb+srv://eternalbot:eF1cloYlSh1UDm9L@cluster0.iggjtiz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "eternalbot")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "")
BOT_USERNAME = environ.get("BOT_USERNAME", "") # your bot username without @
PICS = (environ.get('PICS', 'https://telegra.ph/file/57663ba796ab3bc0b634b.jpg https://telegra.ph/file/c4271632eea7b957d7eaa.jpg https://telegra.ph/file/3e5ade5612b96b3245ad0.jpg https://telegra.ph/file/870b331da70b7242077ea.jpg https://telegra.ph/file/73323bc8852c5ebe2b7c2.jpg https://telegra.ph/file/5f65a3bbb9c574f282400.jpg https://telegra.ph/file/54b1ecfc820efc9f35e86.jpg https://telegra.ph/file/89bf09cc89eb23bba771b.jpg https://telegra.ph/file/5137942f19ad6ea7954bc.jpg https://telegra.ph/file/5449c2a9e299b56a2bece.jpg https://telegra.ph/file/809f4c47684d9641fe901.jpg https://telegra.ph/file/13d2feff69ce1ee1b6c9b.jpg https://telegra.ph/file/f4cef421c9f5c64007b7a.jpg https://telegra.ph/file/beac0cb13865ab5077559.jpg https://telegra.ph/file/4b741ef5f39cc69d83b68.jpg https://telegra.ph/file/d879aa3d983e735e98544.jpg https://telegra.ph/file/78161f2df40b9f98111cd.jpg https://telegra.ph/file/e10cce504cb2b62b6a85d.jpg https://telegra.ph/file/ffaf07f06c3b78636d653.jpg https://telegra.ph/file/db85398f4ff0883fd1702.jpg https://telegra.ph/file/76afbc288f31be3f70a9c.jpg')).split() # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002060836439"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002056340638')).split()]

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filetolinkvjbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002060836439'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = ""
    else:
        URL = ""



# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
