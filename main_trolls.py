#!/usr/bin/env python
# coding: utf-8

from datetime import datetime 
import nltk
import numpy as np
import os, sys
import pandas as pd
import re


def main():
    folder = os.path.join(os.getcwd(), 'data')
    file = os.path.join(folder, 'IRAhandle_tweets_1.csv')
    print(file)
    df = pd.read_csv(file)


    # info:
    # 
    # region: Regio waar de tweet vandaan komt (?)
    # 
    # author: Accountname
    # 
    # language: taal van de tweet
    # 
    # retweet: 0 of 1, dus is het een retweet of niet
    # account_category: RightTroll', 'NonEnglish', 'Fearmonger', 'LeftTroll', 'Unknown', 'HashtagGamer', 'NewsFeed', 'Commercial'
    # 
    # Updates: aantal twitter berichten gepost?
    # 


    df[df['language'] == 'Russian']
    print(df)


if __name__ == '__main__':
    main()
