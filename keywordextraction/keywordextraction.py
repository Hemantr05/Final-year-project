#from nltk import sent_tokenize
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from urllib.request import urlopen
from bs4 import BeautifulSoup
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sqlalchemy import create_engine

import pymysql

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import nltk

nltk.download('punkt')

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
#    print(list(freq.keys()))              # (words)
    words = list(freq.keys())

#    print(list(freq.values()))            # (frequency)
    frequency = list(freq.values())
    #print(frequency)
#    freq.plot(20,cumulative=False)  # graph plot of the word and frquency

    dict = {'word':words,'count':frequency}

    df = pd.DataFrame(dict)
    print(df.head())

    dataFrame = df
   

    # ====================================================== Feed data into MySql database ================================================================
    
    tableName = "project"

    sqlEngine = create_engine('mysql+pymysql://root:root@127.0.0.1/project', pool_recycle=3600)

    dbConnection = sqlEngine.connect()

 

    try:

        frame = dataFrame.to_sql(tableName, dbConnection, if_exists='fail');

    except ValueError as vx:

        print(vx)

    except Exception as ex:   

        print(ex)

    else:

        print("Table %s created successfully."%tableName);   

    finally:

        dbConnection.close()

    # ======================================================== End of Database connection ================================================================

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

    parser.add_argument('--url',type=str,default=None,help='Link to extract keywords')

    parser.add_argument('--text',type=str,default=None,help="Text to extract keywords")

    args = parser.parse_args()
   
#    if args.url is None:

    # For url
    url_text = getText(args.url)
    summaryArr = summarize(url_text,10)

#    else:
    # For text

#        text = getText(args.text)
#    summaryArr = summarize(args.text,2)

"""

    word_token = []

    for i in summaryArr:

        token_sent = sent_tokenize(i)
        for j in token_sent:
            token_word = word_tokenize(j)
#    pos_tagger = nltk.pos_tag(token_word)
            word_token.append(token_word)
     #       print(token_word)
            pos_tagger = nltk.pos_tag(token_word)
            print(pos_tagger)

    #df = pd.read_csv('word_count.csv')
    print(len(df))
    words = df['Words']
    freq = df['Frequency']
    #freq = list(freq)
    #print(len(freq))

    idx = []
    for i in range(230):
        idx.append(i)
    print(idx)
#    print(words,freq)
#    tsne = TSNE(random_state=50).fit_transform(freq)
#    plt.plot(tsne,idx)

"""
