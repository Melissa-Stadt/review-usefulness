# -*- coding: utf-8 -*-
"""
These are some basic text processing functions to be used
to process reviews
"""
import os

import IPython

import numpy as np
import pandas as pd

from num2words import num2words

#This removes the HTML escaped charaters  
from html import unescape

def load_BCmerged():
    # load the data
    test = pd.read_csv('./data/drugsComTest_raw.csv')
    train = pd.read_csv('./data/drugsComTrain_raw.csv')
    merge = [train,test]
    merged_data = pd.concat(merge,ignore_index=True)
    bc_merged = merged_data[merged_data['condition'] == 'Birth Control']
    
    # clean the data
    bc_merged.review = bc_merged.review.apply(clean_review)
    return bc_merged

def frac2words(frac):
    # Input: frac is a string that is a fraction (can be mixed)
    # Output: returns the fraction in words
    temp = frac.split(' ')
    if len(temp) == 2:
        whole = temp[0]
        temp2 = temp[1].split('/') # second number would be fraction
        num = temp2[0]
        denom = temp2[1]
    else:
        whole = 0
        temp2 = frac.split('/')
        num = temp2[0]
        denom = temp2[1]
    
    if whole != 0:
        frac_word = num2words(whole) + ' and ' + num2words(num) + ' over ' + num2words(denom)
    else:
        frac_word = num2words(num) + ' over ' + num2words(denom)
    return frac_word


def example_review(data, nums):
    # from data gives you the review for a given number
    # this is helpful for when testing things to get a subset of reviews
    #
    # Inputs: data you are working from, nums: number or list of numbers
    # Output: review or reviews
    example = data.review.iloc[nums]
    return example


def clean_review(text):
    # given a string removes HTML escape characters
    return unescape(text.strip(' "\'')).replace('\ufeff1', '')
