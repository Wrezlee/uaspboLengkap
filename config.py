# config.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    """Membuat koneksi ke database MySQL"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='pbo_uas',
            user='root',  
            password=''   
        )
        if connection.is_connected():
            print("Koneksi ke database berhasil!")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    """Menutup koneksi database"""
    if connection:
        connection.close()
        print("Koneksi database ditutup.")