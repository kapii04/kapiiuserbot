from os import getenv

API_ID = int(getenv("API_ID", "2176505")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1100725986").split()))
OWNER_ID = int(getenv("OWNER_ID", "1100725986"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://kapiiuserbot:Brebes0705@cluster0.twayrkx.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5941102603:AAEAxoX7WumkEDizmAL0SBgZ6CDgdIpoXYU")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/kapii04/kapiiuserbot")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAiObVt5Xbr300CIqjbb0Vbop4l6tDqlnY22VLKuHBFLbYy8Ce3FvbaCUdummvKPYG_iPQq2nOVS_n9gcEQg9QYd7sspdVm6f4ebG08RIV8DwmR5-N2KRdJJ3NGuaoy4jpvJrIS79L8fpz4AkMv520seucbOIUj8VOt1ULT-Nh-xUMDbILprsYZJUTrSM56NopCW6DMSJA1Pm93KZmj8VpqeoaMMAmg_8w-Zhh9Ab8FxA4X2RZyqdmZrpGFzhZ9t0VXz2h9gcvvcCS_-akUSxzcCwpugSLoXbUrr0zDXrQjykEYQRLFNa7p_jiWjbmGpD1hb8C6CFwK2JzBHFaD7x58AAAAAEGbvuIA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
