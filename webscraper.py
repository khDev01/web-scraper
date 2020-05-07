from bs4 import BeautifulSoup
import requests

url = 'https://atom.io/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

for features in content.find_all('h3'):
    print(features.text)

# Get all links in within a pages <a> tags
# for link in content.find_all('a'):
    # print(link.get('href'))
# Print all text from a page
# print(soup.get_text())
# go to BeautifulSoup doc for more https://www.crummy.com/software/BeautifulSoup/bs4/doc/
