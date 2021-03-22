import streamlit as st
import mysql.connector
from mysql.connector import Error

import numpy as np
import pandas as pd

def run_select():

    st.subheader('메일의 데이터를 검색하는 화면입니다.')

    data_list = ['SPAM', 'Not_SPAM', 'ALL']

    spam = st.radio('확인하고 싶은 메일의 종류를 선택하세요.', data_list)
    if spam == 'SPAM' :
        query = """ select * from SPAM
                    where spam = 1; """
    elif spam == 'Not_SPAM':
        query = """ select * from SPAM
                    where spam = 0; """
    else :
        query = """ select * from SPAM; """
        

    # selected_column_list = st.multiselect('확인하고 싶은 데이터를 선택하세요.',column_list)

    try :
        connection = mysql.connector.connect(
            host = 'database-1.cdxb0pb9vr70.us-east-2.rds.amazonaws.com',
            database = 'yhdb',
            user = 'streamlit',
            password = '1q2w3e4r5t'
        )

        if connection.is_connected() :
            cursor = connection.cursor()

            cursor.execute(query)

            results = cursor.fetchall()

            if st.checkbox('메일 데이터 보기') :
                st.dataframe(results)

    except Error as e :
        print('디비 관련 에러 발생' , e)

    finally :
        cursor.close()
        connection.close()
        print('MySQL 커넥션 종료')