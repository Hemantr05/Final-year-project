#from nltk import sent_tokenize
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from urllib.request import urlopen
from bs4 import BeautifulSoup
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import nltk

nltk.download('punkt')
nltk.download('stopwords')

def getText(url):
    page = urlopen(url).read().decode('utf8', 'ignore')
    soup = BeautifulSoup(page, 'lxml')
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    print("Loaded text.")
    return text.encode('ascii', errors='replace').decode().replace("?","")
#text = getText(articleURL)

def summarize(text, n):
    sents = sent_tokenize(text)
    
    assert n <= len(sents)
    wordSent = word_tokenize(text.lower())
    stopWords = set(stopwords.words('english')+list(punctuation))
    
    wordSent= [word for word in wordSent if word not in stopWords]
    freq = FreqDist(wordSent)
#    print(freq.items())             # (word,frequency)
#    print(freq.keys())              # (words)
#    words = freq.keys()

#    print(freq.values())            # (frequency)
#    frequency = freq.keys()

#    freq.plot(20,cumulative=False)  # graph plot of the word and frquency

    df_fdist = pd.DataFrame.from_dict(freq, orient='index')
    df_fdist.columns = ['Frequency']
    df_fdist.index.name = 'Words'
    print(df_fdist)
    df_fdist.to_csv('./word_count.csv')


    ranking = defaultdict(int)
    
    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]
    sentsIDX = nlargest(n, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sentsIDX)]
#summaryArr = summarize(text, 10)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--url',type=str,help='Link to extract keywords')

    args = parser.parse_args()

    text = getText(args.url)
    summaryArry = summarize(text,20)
