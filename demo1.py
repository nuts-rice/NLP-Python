import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import nps_chat as nps
import os


# twitterSamples = nltk.corpus.twitter_samples
# negTweets = twitter_samples.strings('negative_tweets.json')

teenChat = nps.xml_posts("11-08-teens_706posts.xml")
chatWords = nps.words("11-08-teens_706posts.xml")
chatBigrams = nltk.bigrams(chatWords)
cfd = nltk.ConditionalFreqDist(chatBigrams)
maxConfidence = 100



def calculate_flags(flagList, num=15):
    flagNumber = 0
    tokens = nltk.word_tokenize(flagList)
    # TODO: using a list of flags to be determined,
    # iterate through posts to find instances of any flags
    cfd = nltk.ConditionalFreqDist((target, fileid[:10])
        for fileid in nps.fileids()
        for posts in nps.words(fileid)
        for tokens in [flagList]

        if posts.lower().startswith(tokens))

    print("printing tokens within flaglist" + str(tokens))
    #problem here with "max() arg is an empty sequence" if we try to .tabulate()
    cfd.tabulate()


# def calculate_confidence_index(flagCount, timeElapsed):


def conditional_freq_distrubution():
    cfd = nltk.ConditionalFreqDist((target, fileid[:10])
        for fileid in nps.fileids()
        for posts in nps.words(fileid)
        for target in ['sexy', 'guy']
        if posts.lower().startswith(target))
    cfd.plot()

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=" ")
        word= cfdist[word].max()
    print('\n')


def main():

    postCount = len(teenChat)
    print("Post count: " + " " + str(postCount))
    post0 = teenChat[422]
    print(post0.text)
    print(post0.get('class'))
    print(post0.get('user'))

    print("Printing generated model of text using 'sexy':")
    generate_model(cfd, 'sexy')

    print("Reading in flag list")
    flagFile = open('flagList.txt')
    rawFlag = flagFile.read()
    print("printing max of flaglist: " + max(rawFlag))
    print("Calculating number of flags within chats")
    calculate_flags(rawFlag)

    print("printing conditional frequency distribution")
    conditional_freq_distrubution()


if __name__ == '__main__':
    main()



# def extract_features(post):
