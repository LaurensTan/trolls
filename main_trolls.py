# coding: utf-8

from datetime import datetime
import nltk
import numpy as np
import os, sys
import pandas as pd
import re


def clean_data(df):
    cols = ['publish_date', 'harvested_date']
    df[cols] = df[cols].apply(pd.to_datetime, format='%m/%d/%Y %H:%M')
    df = df[df['language'] == 'English']
    df['content'].dropna(inplace = True)

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
