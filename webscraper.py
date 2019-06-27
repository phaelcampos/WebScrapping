from bs4 import BeautifulSoup
import requests
import json

url= 'http://ethans_fake_twitter_site.surge.sh/'                        #Saving the url on a variable

response = requests.get(url,timeout=5)                                  #Requiring the url
content = BeautifulSoup(response.content,"html.parser")#


#tweet = content.find('p', attrs={"class": "content"}).text#filtering only the tag <p> with the class named "content"//// .text=takes only the content of the <p>

tweetArr = []
for tweet in content.findAll('div', attrs={"class":"tweetcontainer"}):  #Put all the data in a dict
    tweetObject={
        "author": tweet.find('h2', attrs={"class":"author"}).text,
        "date": tweet.find('h5', attrs={"class":"dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class":"content"}).text,
        "likes": tweet.find('p', attrs={"class":"likes"}).text,
        "shares": tweet.find('p', attrs={"class":"shares"}).text
    }
    tweetArr.append((tweetObject))

with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)