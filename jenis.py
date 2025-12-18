import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbo_uas"
)
mycursor = mydb.cursor()

class Jenis:
    def __init__(self):
        self

    def select_data():
        sql = "SELECT nama_jenis FROM jenis"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        data=[]
        for x in myresult:
            data.append(str(x).replace("(","")
                        .replace("'","")
                        .replace(",","")
                        .replace(")","")) #hapus karakter object
        return data