from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","28980049"))
API_HASH = getenv("API_HASH","fdca5bec993fa2e9930b4bd87a494d23")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID","6726372149"))

MONGO_DB_URI = getenv("mongodb+srv://k76734182:Radhe@cluster0.qj64t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN","ll_BOTCHAMBER_ll")
