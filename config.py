from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = 29245477
        self.API_HASH = "0abc83883262245c90ca337b7a0375c4"

        self.BOT_TOKEN = "8462016049:AAFc616pDsbIHi_9oznM5Of8skNyBLhu1VI"
        self.MONGO_URL = "mongodb+srv://musicxrobot:8Up92WwJbgUS39FV@cluster0.ys1jirt.mongodb.net/"

        self.LOGGER_ID = (-1002456565415)
        self.OWNER_ID = 7852686677

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = "BQG-QCUAlMpd_D9Se5jURdlE6p4r8tQ4WzWTRhIFeexJuRHy8XEU0FAEThP3JoG3lOPa3T_tE87QfQKQ4cOD5HQZOn9KzmV1MR02xO2Kv7TfMmMSGnngigPfarZD4KRAkIHR-ewHAF-mLXoyq85ikBzljcBZW5ohHs_Ux3x-CoaafxUdHhefYoo0hbpO2S6uOakbHHw7Q6VCP5yVYDhJDt55stXkcgLgLq5uhv0xKOY5y96yNCh9MO2UQYxdlPeefkffx_OmZqbuDoFe3N29YQ7j2ejJGza6ooTQ5osFQjHIXo_QsDKds6gvHyCYdQDB1IZqauEae0J6fjW6OqldphBc3sJiaAAAAAHjIGUMAA"
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Makima_Bots")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Anime_Chatting_Groups")

        self.AUTO_END: bool = getenv("AUTO_END", True)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", True)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/bractea").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://files.catbox.moe/1cdfqm.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/1cdfqm.jpg")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/1cdfqm.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
