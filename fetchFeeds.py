from ast import parse
import requests
import json


url = "https://manga-scrapper-for-asura-scans-website.p.rapidapi.com/series"

headers = {
    'x-rapidapi-host': "manga-scrapper-for-asura-scans-website.p.rapidapi.com",
    'x-rapidapi-key': "d2f094e3e6mshe0faf209b8e1845p1c9c19jsn21aabd671c19"
    }

response = requests.request("GET", url, headers=headers)

#print(response.text)

api_data = response.text

parse_json = json.loads(api_data)

#titles = parse_json[0]["seriesTitle"]

for id in range(len(parse_json)):
    print(parse_json[id]["seriesTitle"])
    print(parse_json[id]["coverImage"])
    print("\n \n")


