import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6828704120:AAEyWoFhSXMJ5l6UESgdsIxnKy2zR-3yU6Y")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29663344"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1ce180a5008f81cb3e23fd4143fe0f6a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001998448249"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6529179563"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://FILESTORETITAN:srikar@cluster0.epl042j.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002037880479"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝙷𝙴𝙻𝙻𝙾...💖 {first}\n\n 𝙾𝚆𝙽𝙴𝙳 𝙱𝚈 𝚂𝚁𝙼 𝚃𝙴𝙻𝙴 𝙼𝙸𝚇 \n\n 𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 <a href=https://t.me/TITAN_SRM_BOT>𝚃𝙸𝚃𝙰𝙽𝙱𝙾𝚃𝚉</a></b>")
disable_web_page_prewiew=True
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1314613615").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "❤️‍🩹 Hello {first}\n\n✨English👇👇\n<b>You need to join in my Channel/Group to use me\nKindly Please join Channel\nclick on try again\n\n✨Hindi👇👇\nमेरा उपयोग करने के लिए आपको मेरे Channel में Join\nहोगा, कृपया Channel मैं Join करे\n try again pe click karo</b>")
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝙷𝙼𝙼... 𝙰𝙶𝙰𝚁 𝙺𝙳𝚁𝙰𝙼𝙰𝚂 𝙰𝚄𝚁 𝙺𝚄𝙲𝙷 𝙱𝙷𝙸 𝙼𝙾𝚅𝙸𝙴𝚂 𝚈𝙰 𝚂𝙴𝚁𝙸𝙴𝚂\n𝙳𝙴𝙺𝙺 𝙽𝙰 𝙷𝙰𝙸 𝚃𝙷𝙾 𝙲𝙻𝙸𝙲𝙺 𝙺𝙰𝚁𝙾 👇👇❤️‍🩹\n\n👀 𝚂𝚁𝙼 𝚃𝙴𝙻𝙴 𝙼𝙸𝚇 𝙲𝙾𝙼𝙼𝚄𝙽𝙸𝚃𝚈 - <a href=https://t.me/addlist/WRcxtboQq3ExNGFl>𝚂𝚁𝙼_𝚃𝙴𝙻𝙴_𝙼𝙸𝚇</a></b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

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
