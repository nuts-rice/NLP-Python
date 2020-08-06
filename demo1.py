import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import nps_chat as nps

# twitterSamples = nltk.corpus.twitter_samples
# negTweets = twitter_samples.strings('negative_tweets.json')

teenChat = nps.xml_posts("11-08-teens_706posts.xml")


def conditional_freq_distrubution():
    cfd = nltk.ConditionalFreqDist((target, fileid[:10])
        for fileid in nps.fileids()
        for posts in nps.words(fileid)
        for target in ['sexy', 'girl']
        if posts.lower().startswith(target))
    cfd.plot()



def main():
    postCount = len(teenChat)
    print("Post count: " + " " + str(postCount))
    post0 = teenChat[422]
    print(post0.text)
    print(post0.get('class'))
    print(post0.get('user'))
    print("printing conditional frequency distribution")
    conditional_freq_distrubution()

if __name__ == '__main__':
    main()



# def extract_features(post):
