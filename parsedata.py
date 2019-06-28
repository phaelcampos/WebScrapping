import json
with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

word=[]
for i in jsonData:
    if "Friend" in i['tweet']:
        word.append(i['date'])
        word.append(i['likes'])

with open('wordData.json', 'w') as outfile: #creating a Json file to put all the data that was filtered
    json.dump(word, outfile)