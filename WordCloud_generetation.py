import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
import glob

##############################################################

with open('1000021.json', encoding="utf8") as json_data:
    data = json.load(json_data)
    for r in data['TweetsList']:
    	#if ['detail'] in r:
    		fo = open(r['tweetID'] + ".txt","w", encoding="utf8")
    		fo.write(r['detail'])
    		fo.close()

##############################################################################
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
#######################################################################################
text= open('result.txt', "r", encoding="utf8")
data = text.read()

plt.figure(figsize=(20,10))
wordcloud = WordCloud(background_color= 'white', mode="RGB", width = 2000, height = 1000).generate(data)
plt.title("tweetlist")
plt.imshow(wordcloud)
plt.axis("off")
plt.show()








