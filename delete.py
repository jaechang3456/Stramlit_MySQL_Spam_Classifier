import streamlit as st
import mysql.connector
from mysql.connector import Error

def run_delete():

    st.subheader('메일 데이터를 삭제하는 화면입니다.')

    try :
        connection = mysql.connector.connect(
        host = 'database-1.cdxb0pb9vr70.us-east-2.rds.amazonaws.com',
        database = 'yhdb',
        user = 'streamlit',
        password = '1q2w3e4r5t'
        )

        if connection.is_connected() :
            cursor = connection.cursor(dictionary=True)

            search = st.text_input('삭제 하고 싶은 메일의 내용을 검색하세요.')

            query = """ select * from SPAM where text like '%{}%';""".format(search)

            cursor.execute(query)
            results = cursor.fetchall()

            if st.button('검색') :

                for row in results :
                    st.write(row)

    except Error as e :
        print('디비 관련 에러 발생',e)

    finally :
        cursor.close()
        connection.close()
        print('MySQL 커넥션 종료')

    mail_id = st.number_input('메일 아이디 입력', value=1)
    
    if st.button('실행') :

        try :
            connection = mysql.connector.connect(
                host = 'database-1.cdxb0pb9vr70.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = '1q2w3e4r5t'
            )

            if connection.is_connected() :
                cursor = connection.cursor()
                query = """ delete from SPAM
                            where mail_id = %s ; """

                data = (mail_id, )

                cursor.execute(query, data)

                connection.commit()

        except Error as e :
            print('디비 관련 에러 발생' , e)

        finally :
        
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')
