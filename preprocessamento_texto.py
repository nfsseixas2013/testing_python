import re
import nltk
import spacy
import pandas as pd
from wordcloud import WordCloud
from unidecode import unidecode
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk import word_tokenize
from nltk.corpus import stopwords
from spacy.lang.pt.stop_words import STOP_WORDS
