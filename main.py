import psycopg2
import streamlit as st
from services.get_city_names import city_names
from services.plan_vacation import plan_vacation_openai

try:
    conn = psycopg2.connect(
        dbname = st.secrets['database']['database_name'],
        user = st.secrets['database']['user_name'],
        password = st.secrets['database']['password_text'],
        host = st.secrets['database']['host_name'],
        port = st.secrets['database']['port_number'] 
    )

    cursor = conn.cursor()

    print("connection successful")

except psycopg2.Error as e:
    print(f"unable to connect {e}")

'''
Retrieve from table "city" the list of cities and display to
the user in dropdown
allow user to select one city
then with open ai display information of the city 
'''

st.title('Encyclopedia of cities')

city_names_list = city_names(cursor)

selected_city = st.selectbox('Select a city from the list',city_names_list)

st.write('You have selected city: ', selected_city)

plan_vacation_openai(selected_city)