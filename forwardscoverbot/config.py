from dotenv import load_dotenv
from os import path, getenv


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN", "5931268983:AAGYfEnhplOzClt7cUW2ecJPXQQaWIT1lzo")
    ADMINS = int(getenv("ADMINS", "1726966074"))
    DB_PATH = getenv("DB_PATH", "database/database.db")
    GROUP = getenv("GROUP", "https://t.me/+H1IFB3CoN9wxYzhl")
    CHANNEL = getenv("CHANNEL", "https://t.me/fwbbasemelayu")
    KODE = getenv("KODE", "https://github.com/kenkansaja/forwardmediabot")
config = Config()

