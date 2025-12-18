import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbo_uas"
)
mycursor = mydb.cursor()

class Barang:
    def __init__(self):
        self

    def insert_data(val1,val2,val3,val4,val5,val6):
        sql = "INSERT INTO barang (id_barang, jenis, nama_barang, ukuran, stok, harga) VALUES(%s, %s, %s, %s, %s, %s)"
        val = (val1,val2,val3,val4,val5,val6)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan...")

    def tampil_data():
        sql = "SELECT id_barang, jenis, nama_barang, ukuran, stok, harga FROM barang"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    
    def select_data_by_id(val1):
        sql = "SELECT id_barang, jenis, nama_barang, ukuran, stok, harga FROM barang WHERE id_barang = %s"
        val = (val1,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchone()
        return myresult
    
    def update_data(val1,val2,val3,val4,val5,val6):
        sql = "UPDATE barang SET jenis=%s, nama_barang=%s, ukuran=%s, stok=%s, harga=%s WHERE id_barang = %s"
        val = (val1,val2,val3,val4,val5,val6)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate...")

    def delete_data(val1):
        sql = "DELETE FROM barang WHERE id_barang = %s"
        value = (val1,)
        mycursor.execute(sql, value)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil dihapus")

    def cek_nama_ada(nama):
        sql = "SELECT COUNT(*) FROM barang WHERE nama_barang = %s"
        mycursor.execute(sql, (nama,))
        myresult = mycursor.fetchone()
        return myresult[0] > 0
    
    def cek_id_ada(id_barang):
        sql = "SELECT COUNT(*) FROM barang WHERE id_barang = %s"
        mycursor.execute(sql, (id_barang,))
        myresult = mycursor.fetchone()
        return myresult[0] > 0