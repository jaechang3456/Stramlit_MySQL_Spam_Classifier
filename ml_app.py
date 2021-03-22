from tensorflow.keras.layers import Dropout, Dense, Input, SimpleRNN, Embedding
from tensorflow.keras.models import Model, Sequential, load_model
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os
import sys
import tensorflow as tf
import h5py
import sys
import pandas as pd
import seaborn as sns
import urllib.request
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import streamlit as st
import json
from sklearn.metrics import accuracy_score
from keras.utils import np_utils

def run_ml_app() :
    tokenizer = Tokenizer()

    with open('data/wordIndex.json') as json_file:
        word_index = json.load(json_file)
        tokenizer.word_index = word_index
    
    sequences = tokenizer.texts_to_sequences('hgwgqfsa, gwqsa')

    max_len = 5077
    data = pad_sequences(sequences, maxlen = max_len)




    
    model = tf.keras.models.load_model('data/my_model2.h5')

