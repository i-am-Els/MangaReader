import requests
import json


class AsuraScan(object):
    def __init__(self):
        super().__init__()

        self.url = "https://manga-scrapper-for-asura-scans-website.p.rapidapi.com/series"

        self.headers = {
            'x-rapidapi-host': "manga-scrapper-for-asura-scans-website.p.rapidapi.com",
            'x-rapidapi-key': "d2f094e3e6mshe0faf209b8e1845p1c9c19jsn21aabd671c19"
        }

        self.apiDict = dict()

        self.sendRequestAll()

    def sendRequestAll(self):
        response = requests.request("GET", self.url, headers=self.headers)

        #print(response.text)

        self.api_data = response.text

        self.parse_json = json.loads(self.api_data)

        self.apiDict = self.parse_json

        return self.apiDict


#titles = parse_json[0]["seriesTitle"]

# for id in range(len(apiDict)):
#     print(apiDict[id]["seriesTitle"])
#     print(apiDict[id]["coverImage"])
#     print("\n \n")


