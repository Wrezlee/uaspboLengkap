import mysql.connector

def get_connection():
    """
    Membuat dan mengembalikan objek koneksi ke database 'pbo_uas'.
    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      
        database="pbo_uas"  
    )
    return mydb