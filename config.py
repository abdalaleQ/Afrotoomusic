from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/e74815820b06773515851.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/e74815820b06773515851.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/rr_r_v")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/rr_r_v")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5904216848").split()))


FAILED = "https://telegra.ph/file/04b2f1f1c808dc49db35b.jpg"
