from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def init(self):
        self.API_ID = 29245477
        self.API_HASH = "0abc83883262245c90ca337b7a0375c4"

        self.BOT_TOKEN = "8360416637:AAGjdc-snsZpaCKATMZeCm1hXBU22VH4_1s"
        self.MONGO_URL = "mongodb+srv://phrolovaxrobot:p0SFEz825QuqzwTi@cluster0.sy26fqm.mongodb.net/?retryWrites=true&w=majority"

        self.LOGGER_ID = -1002456565415
        self.OWNER_ID = 7654385403

        self.SESSION1 = "BQFnJzYAB4GU36CiFyCAZSMA6XV6Kt6UXNwFlK3mDROMWjehifYw-BpiKT-iK4benswKx_WysIeUDzvAclj6n9ytVeuQj1N318I2rlVy7YNqSTQfLvnuMeXqC--0cXcuBLkDgq-9E4uEcddedzS2CwU9LL7zL-NeV_kRGtaHeHsSZNbY8zD8EQ51sMsLKoqFdnGvgXyEVQ3Hra8ZXYIkZT4Cy0cSBkUIFbX0gp87SPMHD2UEZzgFJuPqbs33_7gxIcfmtCHRpOzR-7oJDNYHlDANqPa0xxWaNxXYI7oEMjC3xY-GDJjT8J9exPgGP5B8T4_wYWfbQNA5ZaGBg-cnJMld2HM5MwAAAAHY2x8OAA"
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
