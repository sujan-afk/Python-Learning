import json
import requests

name = input("Enter a name of artist: ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + name )
a = response.json()
for result in a["results"]:
    print(result["trackName"])
