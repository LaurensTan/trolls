# coding: utf-8

from datetime import datetime
import nltk
import numpy as np
import os, sys
import pandas as pd
import re


def clean_data(df):
    df = df[df['language'] == 'English']
    df['content'].dropna(inplace = True)
    df.drop(['tco1_step1', 'tco2_step1', 'tco3_step1', 'alt_external_id', 'article_url'], axis = 1, inplace = True)
    df.sort_values(by='publish_date', inplace = True)
    df[df['external_author_id'] == 906000000000000000]

def main():
    folder = os.path.join(os.getcwd(), 'data')
    df = pd.DataFrame()
    for i in range(1,2):
        file = os.path.join(folder, 'IRAhandle_tweets_'+str(i)+'.csv')
        dfi = pd.read_csv(file)
        df = df.append(dfi)

    clean_data(df)

    #df[df['language'] == 'Russian']
    print(df.head())




if __name__ == '__main__':
    main()


"""
info:

region: Regio waar de tweet vandaan komt (?)

author: Accountname

language: taal van de tweet

retweet: 0 of 1, dus is het een retweet of niet
account_category: RightTroll', 'NonEnglish', 'Fearmonger', 'LeftTroll', 'Unknown', 'HashtagGamer', 'NewsFeed', 'Commercial'

Updates: aantal twitter berichten gepost?
"""
