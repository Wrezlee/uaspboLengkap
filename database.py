# database.py
import mysql.connector
from mysql.connector import Error
import datetime

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'pbo_uas'
        self.user = 'root'
        self.password = ''
        self.connection = None
        
    def connect(self):
        """Membuat koneksi ke database"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return self.connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None
    
    def disconnect(self):
        """Menutup koneksi database"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def execute_query(self, query, params=None, fetch_one=False):
        """Eksekusi query dan return hasil"""
        result = None
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query, params or ())
                
                if query.strip().upper().startswith('SELECT'):
                    if fetch_one:
                        result = cursor.fetchone()
                    else:
                        result = cursor.fetchall()
                else:
                    connection.commit()
                    result = cursor.lastrowid
                
                cursor.close()
        except Error as e:
            print(f"Error executing query: {e}")
            result = None
        finally:
            self.disconnect()
        
        return result
    
    # Method khusus untuk aplikasi
    def get_barang_by_search(self, keyword):
        """Mencari barang berdasarkan keyword"""
        query = """
        SELECT * FROM barang 
        WHERE nama LIKE %s OR kode LIKE %s OR kategori LIKE %s
        """
        params = (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%')
        return self.execute_query(query, params)
    
    def get_all_barang(self):
        """Mendapatkan semua barang"""
        return self.execute_query("SELECT * FROM barang ORDER BY nama")
    
    def get_kategori(self):
        """Mendapatkan semua kategori unik"""
        result = self.execute_query("SELECT DISTINCT kategori FROM barang WHERE kategori IS NOT NULL")
        return [row['kategori'] for row in result] if result else []
    
    def get_stok_barang(self):
        """Mendapatkan data stok barang"""
        return self.execute_query("""
            SELECT b.id, b.kode, b.nama, b.kategori, b.ukuran, b.warna, 
                   b.harga, COALESCE(s.jumlah, 0) as stok
            FROM barang b
            LEFT JOIN stok s ON b.id = s.barang_id
            ORDER BY b.nama
        """)
    
    def get_riwayat_transaksi(self, bulan=None, tahun=None):
        """Mendapatkan riwayat transaksi"""
        query = "SELECT * FROM penjualan WHERE 1=1"
        params = []
        
        if bulan:
            query += " AND MONTH(tanggal) = %s"
            params.append(bulan)
        if tahun:
            query += " AND YEAR(tanggal) = %s"
            params.append(tahun)
        
        query += " ORDER BY tanggal DESC"
        return self.execute_query(query, params)
    
    def insert_penjualan(self, data):
        """Menyimpan data penjualan baru"""
        query = """
        INSERT INTO penjualan (no_struk, tanggal, member_id, subtotal, diskon, pajak, total, kasir)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data['no_struk'],
            data['tanggal'],
            data['member_id'],
            data['subtotal'],
            data['diskon'],
            data['pajak'],
            data['total'],
            data['kasir']
        )
        return self.execute_query(query, params)
    
    def insert_detail_penjualan(self, penjualan_id, items):
        """Menyimpan detail penjualan"""
        for item in items:
            query = """
            INSERT INTO detail_penjualan (penjualan_id, barang_id, jumlah, harga, subtotal)
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (
                penjualan_id,
                item['barang_id'],
                item['jumlah'],
                item['harga'],
                item['subtotal']
            )
            self.execute_query(query, params)
            
            # Update stok
            self.update_stok(item['barang_id'], -item['jumlah'])
    
    def update_stok(self, barang_id, jumlah):
        """Update stok barang"""
        query = """
        INSERT INTO stok (barang_id, jumlah) 
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE jumlah = jumlah + %s
        """
        params = (barang_id, jumlah, jumlah)
        self.execute_query(query, params)
    
    def get_member(self):
        """Mendapatkan semua member"""
        return self.execute_query("SELECT id, nama FROM member ORDER BY nama")
    
    def generate_no_struk(self):
        """Generate nomor struk otomatis"""
        today = datetime.datetime.now().strftime("%Y%m%d")
        query = "SELECT COUNT(*) as count FROM penjualan WHERE DATE(tanggal) = CURDATE()"
        result = self.execute_query(query, fetch_one=True)
        count = result['count'] + 1 if result else 1
        return f"STR/{today}/{count:04d}"