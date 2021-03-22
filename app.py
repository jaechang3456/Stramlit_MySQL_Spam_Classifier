import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow.keras
from keras.models import Sequential
from keras.layers import Dense
import pickle
import os
import tensorflow as tf
import h5py
from sklearn.ensemble import RandomForestClassifier
import sklearn

from eda_app import run_eda_app
from ml_app import run_ml_app
from insert import run_insert
from selects import run_select
from update import run_update
from delete import run_delete

def main():

    st.title('스팸메일 예측')

    # 사이드바 메뉴
    menu = ['Home','EDA','ML']
    choice = st.sidebar.selectbox('Menu',menu)

    menu2 = ['Insert','Select','Update','Delete']
    choice2 = st.sidebar.selectbox("DataBase",menu2)

    if not st.checkbox('RNN관련 화면을 숨기려면 체크하세요.') :
        
        if choice == 'Home':
            st.write('이 앱은 RNN을 이용하여 메일이 스팸메일인지 아닌지를 예측하는 앱니다.')       
            st.write('왼쪽의 사이드바에서 선택하세요.')


        elif choice == 'EDA' :
            run_eda_app()
        elif choice == 'ML' :
            run_ml_app()

    DB_list = ['DB관련 화면 보기','DB관련 화면 숨기기']

    select = st.radio('DB화면',DB_list)

    if select == 'DB화면 보기' :

        if choice2 == 'Insert' :
            run_insert()
        elif choice2 == 'Select' :
            run_select()
        elif choice2 == 'Update' :
            run_update()
        elif choice2 == 'Delete' :
            run_delete()  


if __name__ == '__main__':
    main()