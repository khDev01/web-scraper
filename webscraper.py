from bs4 import BeautifulSoup
import requests
import json

url = 'https://atom.io/'
response = requests.get(url, timeout=5)
# print(response.status_code) # 200 OK page is present

soup = BeautifulSoup(response.content, "html.parser")

featureArr = []
for features in soup.find_all('h4'):
    # print(features.text)
    featureObj = {
        "feature": features.text
    }
    featureArr.append(featureObj)

with open('featureData.json', 'w') as outfile:
    json.dump(featureArr, outfile)
