import os
from dotenv import load_dotenv

load_dotenv()

RASA_APIKEY = os.getenv("RASA_APIKEY")
OPEN_APIKEY = os.getenv("OPEN_APIKEY")


