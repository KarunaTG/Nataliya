import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '2229357'))
API_HASH = environ.get('API_HASH', '31f183a5a075fd4996cb8ad59e7b794f')
BOT_TOKEN = environ.get('BOT_TOKEN', "5456936845:AAEhuTRE4nmNG4vzkFXgJq72kL8eIyYMW_c")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/2d98bc7fd21faa3578af3.jpg https://graph.org/file/13001261b0ec4e3b7e88c.jpg https://graph.org/file/eccc10c43a3f1a3724999.jpg https://graph.org/file/cecb9bd0f368862f8f9be.jpg https://graph.org/file/182b04c00869949324bcf.jpg https://graph.org/file/17bcfc6388a35e9d36729.jpg https://graph.org/file/f710e0c322cdf4bd77f62.jpg https://graph.org/file/f6cedfdb62ac609c7b7f9.jpg https://graph.org/file/05de921c6afb83d68639d.jpg https://graph.org/file/ed5502db4842822978779.jpg https://graph.org/file/80ad291b955cbf4efee13.jpg https://graph.org/file/05b4a29369c263e645013.jpg https://graph.org/file/bbde34d18b19fc17152f1.jpg https://graph.org/file/bfd9c4426c3829534d5f5.jpg https://graph.org/file/65068693efdd46aedc40c.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/7b22c0b70c00db3106b2c.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/451f038b4e7c2ddd10dc0.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/4fa98ec48a8bf90c758f1.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '794968418').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001535319684').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '794968418').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '5703928596').split()]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Karuna:15122000@cluster0.hrtev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Nataliya_files')
SECONDDB_URI = environ.get('SECONDDB_URI', "mongodb+srv://karunamajeegames2:MwkceSptcImlmOov@cluster.4upztey.mongodb.net/?retryWrites=true&w=majority")

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnshort.net')
SHORTLINK_API = environ.get('SHORTLINK_API', '35740dcc6c2a808be526806338ba29f5f759968a')
SECOND_SHORTLINK_URL = environ.get('SECOND_SHORTLINK_URL', 'gplinks.com')
SECOND_SHORTLINK_API = environ.get('SECOND_SHORTLINK_API', '585ee87eae9c3f497dce24aebebef3ec7700f977')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002081411946').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+zMweRQDyPpo2Yjhl')
MOVIE_GROUP = environ.get('MOVIE_GROUP', 'https://t.me/+HeoPTc1IeFg5NDc1')
SERIES_GROUP = environ.get('SERIES_GROUP', 'https://t.me/+q3y3G8RmrudmNzll')
MAIN_CHANNEL = environ.get('MAIN_CHANNEL', 'https://t.me/TVSeriesCW')
VIP_MEMBERSHIP = environ.get('VIP_MEMBERSHIP', 'https://t.me/MrperfectOffcial/39')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/TVSeriesCW')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Verify_Toturial')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'TVSeriesCW Best Channel In Telegram🚩')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001500025641'))
AUTO_REQUEST = int(environ.get('AUTO_REQUEST', '-1001820924316'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", "4")
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]

LANGUAGES = ["malayalam", "tamil" ,"english", "hindi", "telugu", "kannada"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
