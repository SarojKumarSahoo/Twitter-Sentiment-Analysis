import nltk
import operator 

def getTweetWords(tweet):
    all_words = []
    sTweet=tweet.split()
    return sTweet

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    result=[]
    for k in wordlist.keys():
        result.append([k,wordlist[k]])
    return result

def ngramText(filename): 
    textWords=[]
    f=open(filename,"r")
    line=f.readline()
    while line:
        textWords.extend(getTweetWords(line))
        line=f.readline()
    f.close()
    return textWords

def sortList(x):
    return list(reversed(sorted(x, key=operator.itemgetter(1))))

def mostFreqList(filename,k): 
    d=get_word_features(ngramText(filename))
    l=sortList(d)
    m=[w[0] for w in l[0:k]]
    return m


filename="../data/positive_processed.csv"
#ngram=ngramText(filename)

#print get_words_in_tweets(tweets)
#print mostFreqList(filename,5)
#word_features = get_word_features(get_words_in_tweets(tweets))
