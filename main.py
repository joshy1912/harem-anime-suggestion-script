import requests
import time
from pprint import pprint


time.sleep(4)
response = requests.get("https://api.jikan.moe/v3/genre/anime/35/1")
pprint(response.json())