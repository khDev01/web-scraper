from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.tesco.com/groceries/en-GB/shop/fresh-food/fresh-fruit/all'
response = requests.get(url, timeout=5)
# print(response.status_code) # 200 OK page is present
soup = BeautifulSoup(response.content, "html.parser")

# itemsArr = []
itemheader = soup.find('h3', {"class": "sc-jTzLTM"})
item = itemheader.findChildren("a", recursive=False)

for items in item:
  print(items.text)
#   itemsObj = {
#     "items": items.text
#   }
#   itemsArr.append(itemsObj)
#
# with open('itemsData.json', 'w') as outfile:
#   json.dump(itemsArr, outfile)
#
# li.product-list--list-item
#   product-tile-wrapper
#     product-tile
#     flexi-tile
#       tile-content
#         product-details--wrapper
#           product-details--content
#             h3.sc-jTzLTM
#               a.                             productName
#         product-controls__wrapper
#           form.
#             controls
#               price-details--wrapper
#                 price-control-wrapper        price
#                 price-per-quantity-weight    price/weight
