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
flagFile = open('flagList.txt')
flagList = flagFile.read()




def calculate_flags():
    flagNumber = 0
    tokens = nltk.word_tokenize(flagList)

    # TODO: using a list of flags to be determined,
    # iterate through posts to find instances of any flags
    cfd = nltk.ConditionalFreqDist((tokens, fileid[:10])
        for fileid in nps.fileids()
        for posts in nps.words(fileid)
        for target in [tokens]
        #you need a check if len(samples) < 1
        #you don't need to use a format specifier to get string length
        if posts.lower().startswith(str(target)))
    print("printing flagList " + str(tokens))
    print("cfd values: " + str(cfd.keys()))


    #problem here with "max() arg is an empty sequence" if we try to .tabulate()
    cfd.tabulate(cumulative = True)



# I think that we could use the already annotated corpus of this 
# parts of speech should act as a measure of eagerness and wanting to 
# find out about potential victims 
# we should use OOP design patterns to determine posts
# what would also work would be a function of flagged phrases along with time elapsed
# frequency of posts could work as well.

def calculate_confidence_index():
    cfd = nltk.ConditionalFreqDist((target, fileid[:10])
        for fileid in nps.fileids()
        for posts in nps.xml_posts(fileid)
        for target in ['ynQuestion']
        if (posts.get('class') == 'ynQuestion'))
    cfd.plot()


    # if(flagCount != 0 && timeElapsed != 0)
    # {

    
    # }else{

    
    # }
    print("Printing confidence index as a function"
        "of flagCount and timeElapsed")

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

    print("Printing generated model of text using 'boys':")
    generate_model(cfd, 'boys')

    print("Reading in flag list")
    flagFile = open('flagList.txt')
    rawFlag = flagFile.read()
    print("printing length of flaglist: " + str(len(rawFlag)))
    print("Calculating number of flags within chats")
    print("type of flagList = " + str(type(flagList)))
    #calculate_flags()

    calculate_confidence_index()
    

    print("printing conditional frequency distribution")
    conditional_freq_distrubution()


if __name__ == '__main__':
    main()



# def extract_features(post):
