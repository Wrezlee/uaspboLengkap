import mysql.connector

# Koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbo_uas"
)
mycursor = mydb.cursor()

class Jenis:
    def __init__(self):
        pass

    @staticmethod
    def select_data():
        """Mengambil daftar nama_jenis saja (biasanya untuk combobox)"""
        sql = "SELECT nama_jenis FROM jenis"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        data = []
        for x in myresult:
            # Membersihkan tuple hasil fetchall menjadi string murni
            data.append(str(x[0])) 
        return data

    @staticmethod
    def tampil_data():
        """Mengambil semua kolom (id_jenis dan nama_jenis) untuk ditampilkan di tabel"""
        sql = "SELECT id_jenis, nama_jenis FROM jenis"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

    @staticmethod
    def insert_data(id_jenis, nama_jenis):
        """Menambahkan data jenis baru"""
        sql = "INSERT INTO jenis (id_jenis, nama_jenis) VALUES (%s, %s)"
        val = (id_jenis, nama_jenis)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.rowcount

    @staticmethod
    def select_data_by_id(id_jenis):
        """Mencari satu data jenis berdasarkan ID (untuk fungsi Edit/Hapus)"""
        sql = "SELECT id_jenis, nama_jenis FROM jenis WHERE id_jenis = %s"
        val = (id_jenis,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        return myresult

    @staticmethod
    def update_data(nama_jenis, id_jenis):
        """Memperbarui nama jenis berdasarkan ID"""
        sql = "UPDATE jenis SET nama_jenis = %s WHERE id_jenis = %s"
        val = (nama_jenis, id_jenis)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.rowcount

    @staticmethod
    def delete_data(id_jenis):
        """Menghapus data jenis berdasarkan ID"""
        sql = "DELETE FROM jenis WHERE id_jenis = %s"
        val = (id_jenis,)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.rowcount