from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def init(self):
        self.API_ID = "29245477"
        self.API_HASH = ("0abc83883262245c90ca337b7a0375c4")

        self.BOT_TOKEN = ("")
        self.MONGO_URL = ("")

        self.LOGGER_ID = (-1002456565415)
        self.OWNER_ID = (7654385403)

        self.SESSION1 = ""
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AnimeNexusNetwork/160")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EternalsHelplineBot")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", True)
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://files.catbox.moe/stslbq.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/stslbq.jpg")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/stslbq.jpg")
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
