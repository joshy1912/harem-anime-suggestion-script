import requests
import time
from pprint import pprint as pp


time.sleep(4)
response = requests.get("https://api.jikan.moe/v3/genre/anime/35/1")
pp(response.json())
