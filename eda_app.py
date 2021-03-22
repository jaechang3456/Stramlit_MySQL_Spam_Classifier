import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import tensorflow.keras
import pickle
import os
import tensorflow as tf
import h5py
from wordcloud import WordCloud, STOPWORDS

def run_eda_app() :
    st.subheader('EDA 화면입니다.')
    st.write('RNN 딥러닝 학습에 사용한 데이터를 확인 하실 수 있습니다.')

    df = pd.read_csv('data/emails.csv')

    st.write('학습에 사용한 데이터의 갯수입니다.')
    plt.pie(df['spam'].value_counts(), autopct='%.1f')
    plt.show()
    st.pyplot()

    data = ['SPAM', 'NOT_SPAM','ALL']

    if st.checkbox('데이터를 보려면 클릭하세요.') :
        select = st.radio('보려는 데이터를 선택하세요.', data)
        if select == 'SPAM':
            df = df[lambda x: x['spam'] == 1]
            st.dataframe(df)
        elif select == 'NOT_SPAM':
            df = df[lambda x: x['spam'] == 0]
            st.dataframe(df)
        elif select == 'ALL' :
            st.dataframe(df)










        stop_words = STOPWORDS

        wc = WordCloud(background_color='white', stopwords=stop_words)

        df = df[lambda x: x['spam'] == 1]

        stop_words.add('will')
        stop_words.add('subject')
        text_list = df['text'].str.lower().tolist()
        words_as_one_string = ' '.join(text_list)
        my_words = wc.generate(words_as_one_string)


        st.set_option ( 'deprecation.showPyplotGlobalUse', False)

        if st.checkbox('스팸메일에는 어떤 단어가 많이 사용됐는지 보려면 체크하세요'):
            plt.imshow(my_words)
            plt.axis("off")
            st.pyplot()
    
