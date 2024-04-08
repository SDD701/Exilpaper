import requests

responce = requests.get("https://www.wallpaperflare.com/tag")
print(responce.text)

