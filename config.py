from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 26434153))
API_HASH = getenv("API_HASH", "b7bab20a44886d5207f7781cb6f12fe8")

BOT_TOKEN = getenv("BOT_TOKEN", "7665037614:AAGjLuwFKZ3kF-thARzAO-NIsSFej4aTbPE")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://erkbwrs084:909090@cluster0.qdrfgmb.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 7305205222))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Sohbetikidebir")
