import streamlit as st
import mysql.connector
from mysql.connector import Error

def run_insert():

    st.subheader('새로운 데이터를 삽입하는 항목입니다.')
    st.write('메일 내용을 입력해주시면 추후 학습에 도움이 되어 더 정확한 결과를 얻으실 수 있습니다.')

    text = st.text_input('메일의 내용을 입력해주세요.')
    spam = st.radio('스팸 메일인지 선택해주세요.', ['SPAM', 'Not_SPAM'])

    if spam == 'SPAM' :
        spam = 1
    else :
        spam = 0

    if st.button('저장'):

        try :
            connection = mysql.connector.connect(
                host = 'database-1.cdxb0pb9vr70.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = '1q2w3e4r5t'
            )

            if connection.is_connected() :
                print('연결됨')
                db_info = connection.get_server_info()
                print("MySQL sercer version : ", db_info)

                cursor = connection.cursor()

                query = '''insert into SPAM (text, spam)
                        values (%s, %s);'''

                record = (text, spam)
                
                cursor.execute(query, record)
                connection.commit()

                print('{}개 적용됨'.format(cursor.rowcount))

        except Error as e :
            print('디비 관련 에러 발생' , e)

        finally :
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')