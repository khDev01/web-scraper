import json

with open('featureData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    print(i ['feature'])
