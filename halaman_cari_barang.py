# -*- coding: utf-8 -*-
import mysql.connector
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem


#================= 1. IMPOR HALAMAN LAIN =================
try:
    # Mengimpor kelas HalamanPenjualanBaru dari file yang sudah ada
    from halaman_penjualan_baru import HalamanPenjualanBaru 
except ImportError:
    # Jika file penjualan belum ada, ini akan mencegah crash
    HalamanPenjualanBaru = None
    print("PERINGATAN: Tidak dapat mengimpor HalamanPenjualanBaru. Tombol 'Lanjut' tidak berfungsi.")


# ================= 2. DATABASE CONNECTION =================
def get_connection():
    """Mengembalikan objek koneksi ke database"""
    try:
        # PASTIKAN PENGATURAN KONEKSI INI BENAR
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", # KOSONGKAN jika tidak ada password
            database="pbo_uas" # PASTIKAN NAMA DATABASE BENAR
        )
        # print("DEBUG: Koneksi database berhasil!")
        return conn
    except mysql.connector.Error as err:
        print(f"DEBUG CRITICAL ERROR KONEKSI: Gagal terhubung ke database: {err}")
        QMessageBox.critical(None, "Database Error", f"Gagal terhubung ke database: {err}")
        return None

# ================= 3. CLASS UNTUK KERANJANG SEMENTARA =================
class Keranjang:
    def __init__(self):
        # Keranjang akan menyimpan data dalam format:
        # {id_barang: {'data_barang': {...}, 'qty': N, 'subtotal': X}}
        self.items = {}
    
    def add_item(self, barang_data, qty_to_add=1):
        """Menambahkan atau mengupdate item di keranjang"""
        item_id = str(barang_data['id_barang']) 
        harga = barang_data['harga']
        
        if item_id in self.items:
            current_qty = self.items[item_id]['qty']
            new_qty = current_qty + qty_to_add
            self.items[item_id]['qty'] = new_qty
            self.items[item_id]['subtotal'] = new_qty * harga
        else:
            self.items[item_id] = {
                'data_barang': barang_data,
                'qty': qty_to_add,
                'subtotal': qty_to_add * harga
            }
        
    def get_summary(self):
        """Menghitung total item dan total harga"""
        total_items = sum(item['qty'] for item in self.items.values())
        total_harga = sum(item['subtotal'] for item in self.items.values())
        return total_items, total_harga
        
    def clear(self):
        """Mengosongkan keranjang"""
        self.items = {}

# ================= 4. UI DARI PYUICC5 =================
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(20, 20, 80, 30))
        self.pushButton_back.setObjectName("pushButton_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox_pencarian = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_pencarian.setGeometry(QtCore.QRect(50, 80, 900, 100))
        self.groupBox_pencarian.setObjectName("groupBox_pencarian")
        self.label_2 = QtWidgets.QLabel(self.groupBox_pencarian)
        self.label_2.setGeometry(QtCore.QRect(30, 35, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_pencarian = QtWidgets.QLineEdit(self.groupBox_pencarian)
        self.lineEdit_pencarian.setGeometry(QtCore.QRect(140, 35, 300, 30))
        self.lineEdit_pencarian.setObjectName("lineEdit_pencarian")
        self.pushButton_cari = QtWidgets.QPushButton(self.groupBox_pencarian)
        self.pushButton_cari.setGeometry(QtCore.QRect(450, 35, 100, 30))
        self.pushButton_cari.setObjectName("pushButton_cari")
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox_pencarian)
        self.pushButton_reset.setGeometry(QtCore.QRect(560, 35, 100, 30))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.groupBox_hasil = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_hasil.setGeometry(QtCore.QRect(50, 200, 900, 350))
        self.groupBox_hasil.setObjectName("groupBox_hasil")
        self.tableWidget_hasil = QtWidgets.QTableWidget(self.groupBox_hasil)
        self.tableWidget_hasil.setGeometry(QtCore.QRect(30, 40, 840, 250))
        self.tableWidget_hasil.setObjectName("tableWidget_hasil")
        self.tableWidget_hasil.setColumnCount(0)
        self.tableWidget_hasil.setRowCount(0)
        self.pushButton_tambah_ke_keranjang = QtWidgets.QPushButton(self.groupBox_hasil)
        self.pushButton_tambah_ke_keranjang.setGeometry(QtCore.QRect(30, 300, 201, 35))
        self.pushButton_tambah_ke_keranjang.setObjectName("pushButton_tambah_ke_keranjang")
        self.pushButton_lihat_keranjang = QtWidgets.QPushButton(self.groupBox_hasil)
        self.pushButton_lihat_keranjang.setGeometry(QtCore.QRect(240, 300, 171, 35))
        self.pushButton_lihat_keranjang.setObjectName("pushButton_lihat_keranjang")
        self.groupBox_keranjang = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_keranjang.setGeometry(QtCore.QRect(50, 570, 900, 80))
        self.groupBox_keranjang.setObjectName("groupBox_keranjang")
        self.label_jumlah_barang = QtWidgets.QLabel(self.groupBox_keranjang)
        self.label_jumlah_barang.setGeometry(QtCore.QRect(30, 35, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_jumlah_barang.setFont(font)
        self.label_jumlah_barang.setObjectName("label_jumlah_barang")
        self.label_total_sementara = QtWidgets.QLabel(self.groupBox_keranjang)
        self.label_total_sementara.setGeometry(QtCore.QRect(250, 35, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_total_sementara.setFont(font)
        self.label_total_sementara.setObjectName("label_total_sementara")
        self.pushButton_lanjut_penjualan = QtWidgets.QPushButton(self.groupBox_keranjang)
        self.pushButton_lanjut_penjualan.setGeometry(QtCore.QRect(679, 30, 201, 35))
        self.pushButton_lanjut_penjualan.setObjectName("pushButton_lanjut_penjualan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cari Barang - Pencarian"))
        self.centralwidget.setStyleSheet(_translate("MainWindow", "QWidget#centralwidget { background-color: #E3F2FD; }"))
        self.pushButton_back.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
" \tbackground-color: #757575;\n"
" \tcolor: white;\n"
" \tborder: none;\n"
" \tborder-radius: 5px;\n"
" \tpadding: 5px 10px;\n"
" \tfont: 600 9pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover {\n"
" \tbackground-color: #616161;\n"
"}"))
        self.pushButton_back.setText(_translate("MainWindow", "← Back"))
        self.label.setStyleSheet(_translate("MainWindow", "color: #0D47A1;"))
        self.label.setText(_translate("MainWindow", "CARI BARANG 🔍"))
        self.groupBox_pencarian.setStyleSheet(_translate("MainWindow", "QGroupBox { \n"
" \t\t background-color: white; \n"
" \t\t border: 2px solid #BBDEFB; \n"
" \t\t border-radius: 10px; \n"
" \t\t margin-top: 15px; \n"
" \t\t padding-top: 15px;\n"
" \t\t font: 700 12pt \"Times New Roman\"; \n"
" \t\t color: #1976D2; \n"
" \t\t}\n"
" \t\tQGroupBox::title { \n"
" \t\t subcontrol-origin: margin; \n"
" \t\t subcontrol-position: top center; \n"
" \t\t padding: 0 10px; \n"
" \t\t}"))
        self.groupBox_pencarian.setTitle(_translate("MainWindow", "Pencarian Barang"))
        self.label_2.setText(_translate("MainWindow", "Cari Barang:"))
        self.lineEdit_pencarian.setStyleSheet(_translate("MainWindow", "QLineEdit { border: 1px solid #BBDEFB; border-radius: 6px; padding: 5px; }"))
        self.lineEdit_pencarian.setPlaceholderText(_translate("MainWindow", "Masukkan nama barang, kode, atau kategori..."))
        self.pushButton_cari.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
" \tbackground-color: #2196F3;\n"
" \tcolor: white;\n"
" \tborder: none;\n"
" \tborder-radius: 6px;\n"
" \tpadding: 5px 10px;\n"
" \tfont: 700 10pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover {\n"
" \tbackground-color: #1976D2;\n"
"}"))
        self.pushButton_cari.setText(_translate("MainWindow", "Cari"))
        self.pushButton_reset.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
" \tbackground-color: #FF9800;\n"
" \tcolor: white;\n"
" \tborder: none;\n"
" \tborder-radius: 6px;\n"
" \tpadding: 5px 10px;\n"
" \tfont: 700 10pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover {\n"
" \tbackground-color: #F57C00;\n"
"}"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.groupBox_hasil.setStyleSheet(_translate("MainWindow", "QGroupBox { \n"
" \t\t background-color: white; \n"
" \t\t border: 2px solid #BBDEFB; \n"
" \t\t border-radius: 10px; \n"
" \t\t margin-top: 15px; \n"
" \t\t padding-top: 15px;\n"
" \t\t font: 700 12pt \"Times New Roman\"; \n"
" \t\t color: #1976D2; \n"
" \t\t}\n"
" \t\tQGroupBox::title { \n"
" \t\t subcontrol-origin: margin; \n"
" \t\t subcontrol-position: top center; \n"
" \t\t padding: 0 10px; \n"
" \t\t}"))
        self.groupBox_hasil.setTitle(_translate("MainWindow", "Hasil Pencarian Barang"))
        self.tableWidget_hasil.setStyleSheet(_translate("MainWindow", "QTableWidget {\n"
" \tborder: 1px solid #BBDEFB;\n"
" \tborder-radius: 5px;\n"
" \tbackground-color: white;\n"
"}\n"
"QHeaderView::section {\n"
" \tbackground-color: #2196F3;\n"
" \tcolor: white;\n"
" \tpadding: 5px;\n"
"}"))
        self.pushButton_tambah_ke_keranjang.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
" \tbackground-color: #4CAF50;\n"
" \tcolor: white;\n"
" \tborder: none;\n"
" \tborder-radius: 6px;\n"
" \tpadding: 8px 15px;\n"
" \tfont: 700 11pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover {\n"
" \tbackground-color: #388E3C;\n"
"}"))
        self.pushButton_tambah_ke_keranjang.setText(_translate("MainWindow", "Tambah ke Keranjang"))
        self.pushButton_lihat_keranjang.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
" \tbackground-color: #2196F3;\n"
" \tcolor: white;\n"
" \tborder: none;\n"
" \tborder-radius: 6px;\n"
" \tpadding: 8px 15px;\n"
" \tfont: 700 11pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover {\n"
" \tbackground-color: #1976D2;\n"
"}"))
        self.pushButton_lihat_keranjang.setText(_translate("MainWindow", "Lihat Keranjang"))
        self.groupBox_keranjang.setStyleSheet(_translate("MainWindow", "QGroupBox { \n"
" \t\t background-color: white; \n"
" \t\t border: 2px solid #4CAF50; \n"
" \t\t border-radius: 10px; \n"
" \t\t margin-top: 15px; \n"
" \t\t padding-top: 15px;\n"
" \t\t font: 700 12pt \"Times New Roman\"; \n"
" \t\t color: #2E7D32; \n"
" \t\t}\n"
" \t\tQGroupBox::title { \n"
" \t\t subcontrol-origin: margin; \n"
" \t\t subcontrol-position: top center; \n"
" \t\t padding: 0 10px; \n"
" \t\t}"))
        self.groupBox_keranjang.setTitle(_translate("MainWindow", "Keranjang Sementara"))
        self.label_jumlah_barang.setText(_translate("MainWindow", "Jumlah Barang: 0 item"))
        self.label_total_sementara.setText(_translate("MainWindow", "Total Sementara: Rp 0"))
        self.pushButton_lanjut_penjualan.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
" \tbackground-color: #9C27B0;\n"
" \tcolor: white;\n"
" \tborder: none;\n"
" \tborder-radius: 6px;\n"
" \tpadding: 8px 15px;\n"
" \tfont: 700 11pt \"Times New Roman\";\n"
"}\n"
"QPushButton:hover {\n"
" \tbackground-color: #7B1FA2;\n"
"}"))
        self.pushButton_lanjut_penjualan.setText(_translate("MainWindow", "Lanjut ke Penjualan"))


# ================= 5. CLASS LOGIKA UTAMA =================
class HalamanCariBarang(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent_window = parent # Menyimpan parent window (misal: Dashboard)
        
        # Inisialisasi Data dan Keranjang
        self.keranjang = Keranjang()
        self.all_barang_data = {} 
        self.setup_table()
        self.load_data_barang()
        self.update_keranjang_summary()

        # Koneksi Sinyal (Event Handling)
        self.ui.pushButton_cari.clicked.connect(self.search_barang)
        self.ui.lineEdit_pencarian.returnPressed.connect(self.search_barang)
        self.ui.pushButton_reset.clicked.connect(self.reset_data)
        self.ui.pushButton_tambah_ke_keranjang.clicked.connect(self.add_to_cart)
        self.ui.pushButton_lihat_keranjang.clicked.connect(self.show_cart)
        self.ui.pushButton_lanjut_penjualan.clicked.connect(self.lanjut_penjualan)
        self.ui.pushButton_back.clicked.connect(self.kembali_dashboard)

    def format_rupiah(self, number):
        """Memformat angka menjadi string Rupiah (misalnya Rp 100.000)"""
        return f"Rp {number:,.0f}".replace(",", "#").replace(".", ",").replace("#", ".")

    def setup_table(self):
        t = self.ui.tableWidget_hasil
        t.setColumnCount(5) 
        t.setHorizontalHeaderLabels(["ID Barang", "Nama Barang", "Kategori", "Harga ", "Stok"])
        t.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        t.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch) 
        t.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        t.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        t.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def kembali_dashboard(self):
        """Menutup jendela ini dan menampilkan kembali parent window"""
        self.close()
        if self.parent_window and hasattr(self.parent_window, 'show'):
            self.parent_window.show()

    def update_keranjang_summary(self):
        """Memperbarui label ringkasan keranjang"""
        total_items, total_harga = self.keranjang.get_summary()
        self.ui.label_jumlah_barang.setText(f"Jumlah Barang: {total_items} item")
        self.ui.label_total_sementara.setText(f"Total Sementara: {self.format_rupiah(total_harga)}")

    def load_data_barang(self, search_term=""):
        """Memuat data barang dari DB atau hasil pencarian ke tabel"""
        conn = get_connection()
        if not conn: return

        try:
            cur = conn.cursor(dictionary=True) 
            
            query = """
                SELECT id_barang, nama_barang, jenis, harga, stok
                FROM barang
                WHERE stok > 0
            """

            params = []
            
            if search_term:
                search_like = f"%{search_term}%"
                query += " AND (id_barang LIKE %s OR nama_barang LIKE %s OR jenis LIKE %s)"
                params = [search_like, search_like, search_like]
            
            cur.execute(query, tuple(params))
            rows = cur.fetchall()
            
            self.all_barang_data.clear() 
            t = self.ui.tableWidget_hasil
            t.setRowCount(0)
            
            for row_index, row_data in enumerate(rows):
                self.all_barang_data[row_data['id_barang']] = row_data 
                t.insertRow(row_index)
                
                items = [
                    QTableWidgetItem(row_data['id_barang']),
                    QTableWidgetItem(row_data['nama_barang']),
                    QTableWidgetItem(row_data['jenis']),
                    QTableWidgetItem(self.format_rupiah(row_data['harga'])),
                    QTableWidgetItem(str(row_data['stok']))
                ]
                
                for col, item in enumerate(items):
                    item.setTextAlignment(QtCore.Qt.AlignCenter if col != 1 else QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                    t.setItem(row_index, col, item)
                    
            if not rows and search_term:
                 QMessageBox.information(self, "Hasil", f"Tidak ditemukan barang dengan kata kunci '{search_term}'.")

        except Exception as e:
            print(f"DEBUG CRITICAL ERROR QUERY: {str(e)}")
            QMessageBox.critical(self, "Database Error", f"Gagal memuat data barang: {str(e)}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def search_barang(self):
        search_term = self.ui.lineEdit_pencarian.text().strip()
        self.load_data_barang(search_term)

    def reset_data(self):
        self.ui.lineEdit_pencarian.clear()
        self.load_data_barang()

    def add_to_cart(self):
        selected_rows = self.ui.tableWidget_hasil.selectionModel().selectedRows()
        
        if not selected_rows:
            QMessageBox.warning(self, "Peringatan", "Pilih satu barang dari tabel untuk ditambahkan.")
            return

        row = selected_rows[0].row()
        id_barang = (self.ui.tableWidget_hasil.item(row, 0).text())
        stok_tersedia = int(self.ui.tableWidget_hasil.item(row, 4).text())
        
        if stok_tersedia <= 0:
            QMessageBox.warning(self, "Stok Habis", "Barang ini sudah habis (Stok 0).")
            return
            
        barang_detail = self.all_barang_data.get(id_barang)
        
        if barang_detail:
            qty_to_add = 1 # Default 1
            
            current_cart_qty = self.keranjang.items.get(id_barang, {}).get('qty', 0)
            if (current_cart_qty + qty_to_add) > stok_tersedia:
                QMessageBox.warning(self, "Stok Tidak Cukup", 
                                    f"Stok tersedia: {stok_tersedia}. Anda sudah memiliki {current_cart_qty} di keranjang.")
                return

            self.keranjang.add_item(barang_detail, qty_to_add)
            self.update_keranjang_summary()
            QMessageBox.information(self, "Sukses", f"1 item '{barang_detail['nama_barang']}' berhasil ditambahkan ke keranjang.")
        else:
            QMessageBox.critical(self, "Error", "Detail barang tidak ditemukan.")

    def show_cart(self):
        if not self.keranjang.items:
            QMessageBox.information(self, "Keranjang Kosong", "Keranjang Anda masih kosong.")
            return
            
        summary_text = "### Detail Keranjang:\n"
        for item_id, item in self.keranjang.items.items():
            nama = item['data_barang']['nama_barang']
            qty = item['qty']
            subtotal = self.format_rupiah(item['subtotal'])
            summary_text += f"- {nama} ({item_id}) x {qty} | Subtotal: {subtotal}\n"
            
        total_items, total_harga = self.keranjang.get_summary()
        summary_text += f"\n**TOTAL ITEM: {total_items}**\n"
        summary_text += f"**TOTAL HARGA: {self.format_rupiah(total_harga)}**"
        
        QMessageBox.information(self, "Isi Keranjang Sementara", summary_text)

    def lanjut_penjualan(self):
        """
        FIXED: Membuka jendela HalamanPenjualanBaru dan mentransfer data keranjang.
        """
        if not self.keranjang.items:
            QMessageBox.warning(self, "Keranjang Kosong", "Keranjang kosong. Tambahkan barang terlebih dahulu.")
            return

        if HalamanPenjualanBaru is None:
            QMessageBox.critical(self, "Error", "Kelas 'HalamanPenjualanBaru' tidak ditemukan. Pastikan file terimpor dengan benar.")
            return

        # Sembunyikan jendela pencarian
        self.hide()
        
        try:
            # Kirim data keranjang ke konstruktor HalamanPenjualanBaru
            # Kita perlu memastikan HalamanPenjualanBaru siap menerima initial_cart_items
            self.window_penjualan = HalamanPenjualanBaru(initial_cart_items=self.keranjang.items, parent=self)
            self.window_penjualan.show()
            
            # Kosongkan keranjang di halaman pencarian setelah dikirim
            self.keranjang.clear()
            self.update_keranjang_summary()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal membuka Halaman Penjualan: {str(e)}")
            self.show() # Tampilkan kembali jendela pencarian jika gagal


# ================= 6. RUN APLIKASI =================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Dummy parent class untuk simulasi jika dijalankan sendiri
    class DummyParent(QMainWindow):
        def show(self):
            print("Kembali ke Dashboard")
    
    parent = DummyParent()
    win = HalamanCariBarang(parent)
    win.show()
    sys.exit(app.exec_())