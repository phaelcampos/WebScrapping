from bs4 import BeautifulSoup
import requests
# import json
import csv

url= 'http://ethans_fake_twitter_site.surge.sh/'                        #Saving the url on a variable

response = requests.get(url,timeout=5)                                  #Requiring the url
content = BeautifulSoup(response.content,"html.parser")#

#tweet = content.find('p', attrs={"class": "content"}).text             #filtering only the tag <p> with the class named "content"//// .text=takes only the content of the <p>

for tweet in content.findAll('div', attrs={"class":"tweetcontainer"}):  #Put all the data in a dict
    likes = tweet.find('p', attrs={"class": "likes"}).text  # taking only the numerical part of the likes, and them converting them to a INT
    likes = (int(likes[7:]))

    shares = tweet.find('p', attrs={"class": "shares"}).text  # taking only the numerical part of the shared, and them converting them to a INT
    shares = (int(shares[8:]))

    tweetObject={
        "author": tweet.find('h2', attrs={"class":"author"}).text,
        "date": tweet.find('h5', attrs={"class":"dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class":"content"}).text,
        "likes": likes,
        "shares": shares
    }

    with open('tweetScrap.csv', 'w') as m:  # Creating csv file, to store all the tweet content
        w = csv.DictWriter(m, tweetObject.keys())  # Taking only the dict keys (author, date, etc)
        w.writeheader()  # Setting the header of the file
        w.writerow(tweetObject)  # writing the rest of the data

# with open('twitterData.json', 'w') as outfile: #creating a Json file to put all
#     json.dump(tweetArr, outfile)


