# db_utils.py

import mysql.connector
import streamlit as st
from db import get_db_connection

def save_file_details(user_id, file_name, ipfs_link, encryption_key):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bitlocks_db"
    )
    cursor = conn.cursor()
    
    # Insert into the files table
    sql = "INSERT INTO files (user_id, file_name, ipfs_link, encryption_key) VALUES (%s, %s, %s, %s)"
    values = (user_id, file_name, ipfs_link, encryption_key)
    cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()
