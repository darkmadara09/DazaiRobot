class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 13279715
    API_HASH = "56e198053932ecf216af72a2ddffcd78"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://bwxyihepqyqbwz:180888d0a1d2495e9aff62ae7b16d8dd1c7ec1f6debbd27558cb2eea49f96ced@ec2-52-4-153-146.compute-1.amazonaws.com:5432/dc9u1g5duu57fq"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002139608040)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Obito:Obito@obito.uolt8k3.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/ee28ffa1fa36ac19faa41.jpg"

    SUPPORT_CHAT = "The_Apexx"  # Your Telegram support group chat username where your users will go and bother you

    ARQ_API_KEY = "" #git it form @ARQRobot
    
    ARQ_API_URL = "https://arq.hamker.in" # dont change
    
    TOKEN = "6651687872:AAFPLZBp4P7OEO-Yi-q4YwXNfvx53lQy36Y"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6529892817  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
