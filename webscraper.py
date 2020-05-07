from bs4 import BeautifulSoup
import requests
import json



url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text
    }
    tweetArr.append(tweetObject)
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)








# url = 'https://atom.io/'
# response = requests.get(url, timeout=5)
# content = BeautifulSoup(response.content, "html.parser")
#
#
# featureArr = []
# for features in content.find_all('h4'):
#     # print(features.text.encode())
#     featureArr.append(features.text.encode())
# with open('featureData.json', 'w') as outfile:
#     json.dump(featureArr, outfile)
#
#
#



# Get all links in within a pages <a> tags
# for link in content.find_all('a'):
    # print(link.get('href'))
# Print all text from a page
# print(soup.get_text())
# go to BeautifulSoup doc for more https://www.crummy.com/software/BeautifulSoup/bs4/doc/
