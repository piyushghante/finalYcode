# db.py

import mysql.connector
import streamlit as st

def get_db_connection():
    try:
        conn = mysql.connector.connect(
             host="localhost",
            user="root",
            password="",
            database="bitlocks_db"
        )
        return conn
    except mysql.connector.Error as err:
        st.error(f"Database Connection Error: {err}")
        return None
