# -*- coding: utf-8 -*-
"""
Functions that can be used for text processing and evalutating n-grams
"""
from basic_functions import*

# plotting
import plotly
from plotly import tools
import plotly.graph_objs as go

from collections import defaultdict

import pandas as pd

# text processing
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# spell check 
from spellchecker import SpellChecker
spell = SpellChecker()

def generate_ngrams(text, sw, n_gram):
    # Input: text, sw is stopwords, n_gram is what n-gram number
    # Output: list n-grams for the given inputs
    token = [token for token in text.lower().split(" ") if token != "" if token not in sw]
    ngrams = zip(*[token[i:] for i in range(n_gram)])
    return [" ".join(ngram) for ngram in ngrams]

def freq_ngrams(data, sw, n_gram):
    # Input: data, stopwords, n for n_gram
    # Output: sorted dictionary with the n-grams and their frequency
    fd = defaultdict(int)
    for sent in data["review"]:
        for word in generate_ngrams(sent, sw, n_gram):
            fd[word] +=1
    fd_sorted = pd.DataFrame(sorted(fd.items(), key=lambda x:x[1])[::-1])
    fd_sorted.columns = ["word", "count"]
    return fd_sorted

## custom function for horizontal bar chart ##
def set_bar_chart(df, color = 'blue'):
    trace = go.Bar(
        y=df["word"].values[::-1],
        x=df["count"].values[::-1],
        showlegend=False,
        orientation = 'h',
        marker=dict(
            color=color,
        ),
    )
    return trace

def lemmatize(text):
    # using WordNetLemmatizer returns the review lemmatized
    word_list = nltk.word_tokenize(text)
    lemma_words = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
    return lemma_words

def count_misspelled(text):
    word_list = nltk.word_tokenize(text)
    misspelled = spell.unknown(word_list)
    return len(misspelled)
