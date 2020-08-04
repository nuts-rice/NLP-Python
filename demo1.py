import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import nps_chat as nps

# twitterSamples = nltk.corpus.twitter_samples
# negTweets = twitter_samples.strings('negative_tweets.json')
teenChat = nps.xml_posts("11-08-teens_706posts.xml")
postCount = len(teenChat)
print("Post count: " + " " + str(postCount))
post0 = teenChat[422]
print(post0.text)
print(post0.get('class'))
print(post0.get('user'))


def conditional_freq_distrubution():
cfd = nltk.ConditionalFreqDist((target)
    for word in teenChat
    for target in ['girl', 'boy']
    if word.findall(target))
cfd.plot()

# def main():
#     conditional_freq_distrubution()


#
#
# def extract_features(post):
#
