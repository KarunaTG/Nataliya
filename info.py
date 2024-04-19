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
BOT_TOKEN = environ.get('BOT_TOKEN', "5425847881:AAF-vNcW1Hjl_s8THDUurrcjS9ePMEfPb_I")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://te.legra.ph/file/10cf9c67c0d5ef3c2ead9.jpg https://te.legra.ph/file/d44d6cc936d906f0071bc.jpg https://te.legra.ph/file/8a5213082d552d95fd8b7.jpg https://te.legra.ph/file/3ca6d7da7fbc91ec7bdcd.jpg https://te.legra.ph/file/d4cfc088ca6f5d56df31c.jpg https://te.legra.ph/file/4a06d75e21ffd98872de6.jpg https://te.legra.ph/file/1cf3c65a9298a2c1ff2a1.jpg https://te.legra.ph/file/b1b03f922126008e15067.jpg https://te.legra.ph/file/273c416ccfc668da889b6.jpg https://te.legra.ph/file/306f3000cf595472df2f5.jpg https://te.legra.ph/file/b5094d4beca34929c4603.jpg https://te.legra.ph/file/239d4386d9af51fad47e2.jpg https://te.legra.ph/file/ab1a1c9d09c435c30748f.jpg https://te.legra.ph/file/7a9b2b453530311fd0f2f.jpg https://te.legra.ph/file/f5f3afb0f7f077ff2a6ab.jpg https://te.legra.ph/file/3f1ef429fb3d423e5e6f7.jpg https://te.legra.ph/file/53e8129d1fa398b42442d.jpg https://te.legra.ph/file/c711ef8b4027b30729c16.jpg https://te.legra.ph/file/d771aaa61a24622590637.jpg https://te.legra.ph/file/dfc6471e7fbc8a6eefec6.jpg https://te.legra.ph/file/8786af668cb9759d02075.jpg https://te.legra.ph/file/cd309c362f3c51cf6215a.jpg https://te.legra.ph/file/8c453e04aa52f70104d2f.jpg https://te.legra.ph/file/877c45feb170c27147edd.jpg https://te.legra.ph/file/dbeef1a216c1bac247cda.jpg https://te.legra.ph/file/81450af52f9c93a495f1f.jpg https://te.legra.ph/file/72e308459d239f5824bf1.jpg https://te.legra.ph/file/73c7443606cb896716445.jpg https://te.legra.ph/file/23c162a43981592f9c6e5.jpg https://te.legra.ph/file/9c086a0780f863c094cbd.jpg https://te.legra.ph/file/4b82ce29383c614eaf0b0.jpg https://te.legra.ph/file/4794471cc79f90494ba31.jpg https://te.legra.ph/file/f475bb950100047dfd9c3.jpg https://te.legra.ph/file/cdc3670be8b7291adccfd.jpg https://te.legra.ph/file/6c774764602e9b19236b5.jpg https://te.legra.ph/file/b0bf592defba934048930.jpg https://te.legra.ph/file/1759614f1de92fa19b4c4.jpg https://te.legra.ph/file/336dc215072241afb185d.jpg https://te.legra.ph/file/63fede32e135bbe8ca7b9.jpg https://te.legra.ph/file/e4ae49d67321c4d5c7684.jpg https://te.legra.ph/file/bed4a846e33e7fcbbcec9.jpg https://te.legra.ph/file/ca38bcbf4b9b21c3511f9.jpg https://te.legra.ph/file/e23f6637565bffa6af327.jpg https://te.legra.ph/file/6fcd23d181eb988be7d65.jpg https://te.legra.ph/file/f1694893cb4c856ba9156.jpg https://te.legra.ph/file/dc3bd62c7f8627c2eece4.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/dc3bd62c7f8627c2eece4.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://te.legra.ph/file/6c774764602e9b19236b5.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/6c774764602e9b19236b5.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '794968418').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
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
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://natashamajee:UTtgMu3qoV3PMxxQ@cluster.q8yyke6.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
SECONDDB_URI = environ.get('SECONDDB_URI', "mongodb+srv://natashamajee:UTtgMu3qoV3PMxxQ@cluster.q8yyke6.mongodb.net/?retryWrites=true&w=majority")

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'easysky.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '546326320a3c0a8fdc061f56ca40972e1e35682f')
SECOND_SHORTLINK_URL = environ.get('SECOND_SHORTLINK_URL', 'easysky.in')
SECOND_SHORTLINK_API = environ.get('SECOND_SHORTLINK_API', 'c0c9fb160a5d33bb141ce117e2cce939a36a9682')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+IzoiHCBItzY4NTI1')
MOVIE_GROUP = environ.get('MOVIE_GROUP', 'https://t.me/+IzoiHCBItzY4NTI1')
SERIES_GROUP = environ.get('SERIES_GROUP', 'https://t.me/+IzoiHCBItzY4NTI1')
MAIN_CHANNEL = environ.get('MAIN_CHANNEL', 'https://t.me/Rubina_Updates')
VIP_MEMBERSHIP = environ.get('VIP_MEMBERSHIP', 'https://t.me/Rubina_Updates')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Rubina_Updates')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Rubina_Updates')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
MSG_ALRT = environ.get('MSG_ALRT', 'Who Is Your Favourite Pornstar')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001500025641'))
AUTO_REQUEST = int(environ.get('AUTO_REQUEST', '-1001820924316'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", "4")
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

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
