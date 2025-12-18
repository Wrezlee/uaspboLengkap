# -*- coding: utf-8 -*-
import sys
import mysql.connector
from ukuran import Ukuran
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QHeaderView


# ================= DATABASE CONNECTION =================
def get_connection():
    """Mengembalikan objek koneksi ke database"""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pbo_uas"
        )
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        QMessageBox.critical(None, "Database Error", f"Gagal terhubung ke database: {err}")
        return None

# ================= MODUL BARANG =================
class Barang:
    @staticmethod
    def get_all_barang():
        conn = get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_barang, nama_barang, ukuran, harga, stok FROM barang WHERE stok > 0")
            results = cursor.fetchall()
            conn.close()
            return results
        except Exception as e:
            print(f"Error get_all_barang: {e}")
            if conn and conn.is_connected(): conn.close()
            return []
        
    @staticmethod
    def get_ukuran_by_nama(nama_barang):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT DISTINCT ukuran FROM barang WHERE nama_barang = %s AND stok > 0",
            (nama_barang,)
        )
        data = [row[0] for row in cursor.fetchall()]
        conn.close()
        return data

    @staticmethod
    def update_stok_by_nama_ukuran(nama, ukuran, qty):
        conn = get_connection()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE barang
                SET stok = stok - %s
                WHERE nama_barang = %s AND ukuran = %s
            """, (qty, nama, ukuran))
            conn.commit()
            conn.close()
            return True
        except:
            conn.close()
            return False


# ================= UI DIALOG TAMBAH BARANG =================
class Ui_Dialog_TambahBarang(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 301, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 70, 411, 261))
        self.groupBox.setObjectName("groupBox")
        # Nama Barang
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 100, 25))
        self.label_2.setFont(QtGui.QFont("Times New Roman", 11))
        self.label_2.setObjectName("label_2")
        self.comboBox_barang = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_barang.setGeometry(QtCore.QRect(140, 40, 230, 30))
        self.comboBox_barang.setObjectName("comboBox_barang")
        # Ukuran
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 100, 25))
        self.label_3.setFont(QtGui.QFont("Times New Roman", 11))
        self.label_3.setObjectName("label_3")
        self.comboBox_ukuran = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ukuran.setGeometry(QtCore.QRect(140, 90, 100, 30))
        self.comboBox_ukuran.setObjectName("comboBox_ukuran")
        # Warna
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(260, 90, 80, 25))
        self.label_4.setFont(QtGui.QFont("Times New Roman", 11))
        self.label_4.setObjectName("label_4")
        self.comboBox_warna = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_warna.setGeometry(QtCore.QRect(310, 90, 60, 30))
        self.comboBox_warna.setObjectName("comboBox_warna")
        # Harga Satuan
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 100, 25))
        self.label_5.setFont(QtGui.QFont("Times New Roman", 11))
        self.label_5.setObjectName("label_5")
        self.lineEdit_harga = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_harga.setGeometry(QtCore.QRect(140, 140, 150, 30))
        self.lineEdit_harga.setReadOnly(True)
        self.lineEdit_harga.setObjectName("lineEdit_harga")
        # Jumlah (Qty)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 100, 25))
        self.label_6.setFont(QtGui.QFont("Times New Roman", 11))
        self.label_6.setObjectName("label_6")
        self.spinBox_jumlah = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_jumlah.setGeometry(QtCore.QRect(140, 190, 80, 30))
        self.spinBox_jumlah.setMinimum(1)
        self.spinBox_jumlah.setMaximum(100)
        self.spinBox_jumlah.setProperty("value", 1)
        self.spinBox_jumlah.setObjectName("spinBox_jumlah")
        # Sub Total
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(230, 190, 71, 21))
        self.label_7.setFont(QtGui.QFont("Times New Roman", 11))
        self.label_7.setObjectName("label_7")
        self.lineEdit_subtotal = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_subtotal.setGeometry(QtCore.QRect(310, 190, 80, 30))
        self.lineEdit_subtotal.setReadOnly(True)
        self.lineEdit_subtotal.setObjectName("lineEdit_subtotal")
        # Tombol
        self.pushButton_simpan = QtWidgets.QPushButton(Dialog)
        self.pushButton_simpan.setGeometry(QtCore.QRect(150, 340, 100, 35))
        self.pushButton_simpan.setObjectName("pushButton_simpan")
        self.pushButton_batal = QtWidgets.QPushButton(Dialog)
        self.pushButton_batal.setGeometry(QtCore.QRect(260, 340, 100, 35))
        self.pushButton_batal.setObjectName("pushButton_batal")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tambah Barang"))
        self.label.setText(_translate("Dialog", "TAMBAH BARANG"))
        self.groupBox.setTitle(_translate("Dialog", "Pilih Barang"))
        self.label_2.setText(_translate("Dialog", "Nama Barang:"))
        self.label_3.setText(_translate("Dialog", "Ukuran:"))
        self.label_4.setText(_translate("Dialog", "Warna:"))
        self.label_5.setText(_translate("Dialog", "Harga Satuan:"))
        self.label_6.setText(_translate("Dialog", "Jumlah:"))
        self.label_7.setText(_translate("Dialog", "Sub Total"))
        self.pushButton_simpan.setText(_translate("Dialog", "Simpan"))
        self.pushButton_batal.setText(_translate("Dialog", "Batal"))

class DialogTambahBarang(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_TambahBarang()
        self.ui.setupUi(self)
        self.barang_data = {}
        self.selected_data = None

        self.ui.comboBox_barang.currentIndexChanged.connect(self.load_barang_details)
        self.ui.spinBox_jumlah.valueChanged.connect(self.calculate_subtotal)
        self.ui.pushButton_simpan.clicked.connect(self.simpan_dan_tutup)
        self.ui.pushButton_batal.clicked.connect(self.reject)

        self.load_data_barang()
        self.ui.comboBox_barang.currentIndexChanged.connect(self.load_barang_details)
        self.getDataUkuran()

    def load_data_barang(self):
        try:
            data_barang = Barang.get_all_barang()
            self.ui.comboBox_barang.clear()
            for row in data_barang:
                kode_barang, nama_barang, ukuran, harga_jual, stok = row
                display_name = f"{nama_barang} (Stok: {stok})"
                self.ui.comboBox_barang.addItem(display_name, kode_barang)
                self.barang_data[kode_barang] = {
                    'id_barang': kode_barang,
                    'nama_barang': nama_barang,
                    'ukuran': ukuran,
                    'harga': int(harga_jual),
                    'stok': int(stok)
                }
            self.ui.comboBox_warna.addItems(["Hitam", "Putih", "Biru", "Merah", "Hijau"])
            if self.ui.comboBox_barang.count() > 0:
                self.load_barang_details()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal memuat data barang: {str(e)}")

    def getDataUkuran(self):
        data=Ukuran.select_data()
        self.ui.comboBox_ukuran.addItems(data)

    def load_barang_details(self):
        idx = self.ui.comboBox_barang.currentIndex()
        if idx < 0:
            return

        id_barang = self.ui.comboBox_barang.itemData(idx)
        barang = self.barang_data.get(id_barang)

        if not barang:
            return

        nama_barang = barang['nama_barang']

        # ===== FILTER UKURAN =====
        self.ui.comboBox_ukuran.clear()
        ukuran_list = Barang.get_ukuran_by_nama(nama_barang)
        self.ui.comboBox_ukuran.addItems(ukuran_list)

        # ===== SET DATA =====
        self.ui.lineEdit_harga.setText(
            f"Rp {barang['harga']:,}".replace(",", ".")
        )

        self.ui.spinBox_jumlah.setMaximum(barang['stok'])
        self.ui.spinBox_jumlah.setValue(1)

        self.calculate_subtotal()


    def calculate_subtotal(self):
        idx = self.ui.comboBox_barang.currentIndex()
        if idx >= 0:
            id_barang = self.ui.comboBox_barang.itemData(idx)
            if id_barang in self.barang_data:
                harga = self.barang_data[id_barang]['harga']
                jumlah = self.ui.spinBox_jumlah.value()
                subtotal = harga * jumlah
                self.ui.lineEdit_subtotal.setText(f"Rp {subtotal:,}".replace(",", "."))

    def simpan_dan_tutup(self):
        idx = self.ui.comboBox_barang.currentIndex()
        if idx < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih barang terlebih dahulu.")
            return
        id_barang = self.ui.comboBox_barang.itemData(idx)
        barang = self.barang_data[id_barang]
        qty = self.ui.spinBox_jumlah.value()
        if qty > barang['stok']:
            QMessageBox.warning(self, "Stok Tidak Cukup", f"Stok tersedia: {barang['stok']}")
            return
        self.selected_data = {
            'id_barang': barang['id_barang'],
            'nama_barang': barang['nama_barang'],
            'ukuran': self.ui.comboBox_ukuran.currentText(),
            'warna': self.ui.comboBox_warna.currentText(),
            'harga': barang['harga'],
            'qty': qty,
            'subtotal': barang['harga'] * qty,
            'stok': barang['stok']
        }
        self.accept()

    def get_selected_data(self):
        return self.selected_data

# ================== IMPORT WINDOW PEMBAYARAN =================
from window_pembayaran_qris import WindowProsesPembayaran

# ================= UI MAIN WINDOW =================
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setStyleSheet("background-color: #E3F2FD;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # Tombol Back
        self.pushButton_back = QtWidgets.QPushButton("← Back", self.centralwidget)
        self.pushButton_back.setGeometry(20, 20, 100, 35)
        self.pushButton_back.setStyleSheet("background-color: #FF9800;")
        # Judul
        self.label = QtWidgets.QLabel("TRANSAKSI PENJUALAN", self.centralwidget)
        self.label.setGeometry(250, 15, 500, 50)
        self.label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        # INFORMASI
        self.groupBox_pelanggan = QtWidgets.QGroupBox("Informasi", self.centralwidget)
        self.groupBox_pelanggan.setGeometry(50, 80, 900, 100)
        QtWidgets.QLabel("Role:", self.groupBox_pelanggan).setGeometry(30, 40, 100, 25)
        self.comboBox_member = QtWidgets.QComboBox(self.groupBox_pelanggan)
        self.comboBox_member.setGeometry(120, 40, 200, 30)
        self.comboBox_member.addItems(["Umum", "Member"])
        QtWidgets.QLabel("Tanggal:", self.groupBox_pelanggan).setGeometry(400, 40, 100, 25)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_pelanggan)
        self.dateEdit.setGeometry(480, 40, 160, 30)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        # DAFTAR BARANG
        self.groupBox_barang = QtWidgets.QGroupBox("Daftar Barang", self.centralwidget)
        self.groupBox_barang.setGeometry(50, 200, 900, 300)
        self.tableWidget_barang = QtWidgets.QTableWidget(self.groupBox_barang)
        self.tableWidget_barang.setGeometry(30, 40, 840, 200)
        self.pushButton_tambah = QtWidgets.QPushButton("Tambah Barang", self.groupBox_barang)
        self.pushButton_tambah.setGeometry(30, 250, 170, 35)
        self.pushButton_hapus = QtWidgets.QPushButton("Hapus Barang", self.groupBox_barang)
        self.pushButton_hapus.setGeometry(220, 250, 170, 35)
        self.pushButton_hapus.setStyleSheet("background-color: #F44336;")
        # PEMBAYARAN
        self.groupBox_total = QtWidgets.QGroupBox("Pembayaran", self.centralwidget)
        self.groupBox_total.setGeometry(50, 520, 900, 150)
        QtWidgets.QLabel("Subtotal:", self.groupBox_total).setGeometry(30, 40, 100, 25)
        self.lineEdit_subtotal = QtWidgets.QLineEdit(self.groupBox_total)
        self.lineEdit_subtotal.setGeometry(120, 40, 150, 30)
        self.lineEdit_subtotal.setReadOnly(True)
        self.lineEdit_subtotal.setText("Rp 0")
        QtWidgets.QLabel("Diskon (%):", self.groupBox_total).setGeometry(310, 40, 120, 25)
        self.lineEdit_diskon = QtWidgets.QLineEdit(self.groupBox_total)
        self.lineEdit_diskon.setGeometry(420, 40, 80, 30)
        self.lineEdit_diskon.setText("0")
        QtWidgets.QLabel("Pajak (%):", self.groupBox_total).setGeometry(540, 40, 120, 25)
        self.lineEdit_pajak = QtWidgets.QLineEdit(self.groupBox_total)
        self.lineEdit_pajak.setGeometry(650, 40, 80, 30)
        self.lineEdit_pajak.setText("0")
        QtWidgets.QLabel("Total:", self.groupBox_total).setGeometry(30, 90, 100, 25)
        self.lineEdit_total = QtWidgets.QLineEdit(self.groupBox_total)
        self.lineEdit_total.setGeometry(120, 90, 200, 35)
        self.lineEdit_total.setReadOnly(True)
        self.lineEdit_total.setText("Rp 0")
        self.pushButton_bayar = QtWidgets.QPushButton("PROSES BAYAR", self.groupBox_total)
        self.pushButton_bayar.setGeometry(720, 70, 160, 45)
        MainWindow.setCentralWidget(self.centralwidget)

# ================= LOGIKA UTAMA =================
class HalamanPenjualanBaru(QtWidgets.QMainWindow):
    def __init__(self, initial_cart_items=None, parent=None):
        super().__init__()
        self.parent_window = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_table()
        self.setup_events()
        self.diskon_hari_besar()

        if initial_cart_items:
            self.load_cart_items(initial_cart_items)


    def setup_table(self):
        t = self.ui.tableWidget_barang
        t.setColumnCount(7)
        t.setHorizontalHeaderLabels(["ID Barang", "Nama", "Ukuran", "Warna", "Harga", "Qty", "Subtotal"])
        t.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        t.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        t.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        t.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        t.setColumnHidden(0, True)

    def setup_events(self):
        self.ui.pushButton_tambah.clicked.connect(self.tambah_barang)
        self.ui.pushButton_hapus.clicked.connect(self.hapus_barang)
        self.ui.pushButton_back.clicked.connect(self.kembali_dashboard)
        self.ui.pushButton_bayar.clicked.connect(self.proses_bayar)
        self.ui.lineEdit_diskon.textChanged.connect(self.hitung_total)
        self.ui.lineEdit_pajak.textChanged.connect(self.hitung_total)
        self.ui.dateEdit.dateChanged.connect(self.diskon_hari_besar)
        self.ui.comboBox_member.currentTextChanged.connect(self.diskon_member)

    def diskon_member(self, role):
        if role == "Member":
            self.ui.lineEdit_diskon.setText("10")
        else:
            self.ui.lineEdit_diskon.setText("0")

        self.hitung_total()

    def diskon_hari_besar(self):
        tanggal = self.ui.dateEdit.date().toString("dd-MM")
        diskon = {"01-01": 20, "17-08": 25, "25-12": 15}  # contoh diskon hari besar
        self.ui.lineEdit_diskon.setText(str(diskon.get(tanggal, 0)))
        self.hitung_total()

    def tambah_barang(self):
        dialog = DialogTambahBarang(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            data = dialog.get_selected_data()
            if data:
                self.tambah_ke_table(data)
                self.hitung_total()

    def load_cart_items(self, cart_items):
        for item_id, item in cart_items.items():
            data_barang = item['data_barang']
            qty = item['qty']

            data = {
                'id_barang': data_barang['id_barang'],
                'nama_barang': data_barang['nama_barang'],
                'ukuran': '-',   
                'warna': '-',   
                'harga': data_barang['harga'],
                'qty': qty,
                'subtotal': data_barang['harga'] * qty,
                'stok': data_barang['stok']
            }

            self.tambah_ke_table(data)

        self.hitung_total()

    def tambah_ke_table(self, data):
        t = self.ui.tableWidget_barang
        row = t.rowCount()
        t.insertRow(row)
        t.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id_barang']))
        t.setItem(row, 1, QtWidgets.QTableWidgetItem(data['nama_barang']))
        t.setItem(row, 2, QtWidgets.QTableWidgetItem(data['ukuran']))
        t.setItem(row, 3, QtWidgets.QTableWidgetItem(data['warna']))
        t.setItem(row, 4, QtWidgets.QTableWidgetItem(f"Rp {data['harga']:,}".replace(",", ".")))
        t.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data['qty'])))
        t.setItem(row, 6, QtWidgets.QTableWidgetItem(f"Rp {data['subtotal']:,}".replace(",", ".")))

    def hapus_barang(self):
        t = self.ui.tableWidget_barang
        selected = t.currentRow()
        if selected >= 0:
            t.removeRow(selected)
            self.hitung_total()

    def hitung_total(self):
        subtotal = 0
        t = self.ui.tableWidget_barang
        for row in range(t.rowCount()):
            item = t.item(row, 6)
            if item:
                value = int(item.text().replace("Rp ", "").replace(".", ""))
                subtotal += value
        try:
            diskon = float(self.ui.lineEdit_diskon.text())
        except: diskon = 0
        try:
            pajak = float(self.ui.lineEdit_pajak.text())
        except: pajak = 0
        total = subtotal - (diskon/100*subtotal) + (pajak/100*subtotal)
        self.ui.lineEdit_subtotal.setText(f"Rp {subtotal:,}".replace(",", "."))
        self.ui.lineEdit_total.setText(f"Rp {int(total):,}".replace(",", "."))

    def proses_bayar(self):
        if self.ui.tableWidget_barang.rowCount() == 0:
            QMessageBox.warning(self, "Peringatan", "Belum ada barang dalam transaksi.")
            return
        total_text = self.ui.lineEdit_total.text()
        total_bersih = int(total_text.replace("Rp ", "").replace(".", ""))
        pembayaran_window = WindowProsesPembayaran(total_bersih, self)
        if pembayaran_window.exec_() == QtWidgets.QDialog.Accepted:
            metode = pembayaran_window.get_metode()
            bayar = pembayaran_window.get_bayar()         
            kembalian = pembayaran_window.get_kembalian() 
            if self.simpan_transaksi(total_bersih, bayar, kembalian, metode):
                QMessageBox.information(self, "Sukses", "Transaksi berhasil!")

                from cetak_struk import CetakStrukWindow    
                self.cetak_window = CetakStrukWindow(self.last_id_penjualan)
                self.cetak_window.show()
                             
                self.reset_form()


    def simpan_transaksi(self, total, bayar, kembalian, metode):
        try:
            conn = get_connection()
            if not conn: return False
            cursor = conn.cursor()
            # Insert header transaksi
            subtotal = int(
                self.ui.lineEdit_subtotal.text()
                .replace("Rp ", "")
                .replace(".", "")
            )
            cursor.execute("""INSERT INTO penjualan (tanggal, role, total, bayar, kembalian, diskon, pajak, subtotal, harga) VALUES (CURDATE(), %s, %s, %s, %s, %s, %s, %s, %s)""", (
                self.ui.comboBox_member.currentText(),  # role
                total,
                bayar,
                kembalian,
                int(self.ui.lineEdit_diskon.text() or 0),
                int(self.ui.lineEdit_pajak.text() or 0),
                subtotal,
                total
            ))
            id_penjualan = cursor.lastrowid        
            self.last_id_penjualan = id_penjualan    
            # Insert detail
            t = self.ui.tableWidget_barang
            for row in range(t.rowCount()):
                nama_barang = t.item(row, 1).text()
                ukuran = t.item(row, 2).text()
                warna = t.item(row, 3).text()
                harga = int(t.item(row, 4).text().replace("Rp ", "").replace(".", ""))
                qty = int(t.item(row, 5).text())
                subtotal = int(t.item(row, 6).text().replace("Rp ", "").replace(".", ""))
                cursor.execute("""
                    INSERT INTO detail_penjualan
                    (id_penjualan, nama_barang, ukuran, warna, qty, subtotal, harga)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (id_penjualan, nama_barang, ukuran, warna, qty, subtotal, harga ))
                Barang.update_stok_by_nama_ukuran(nama_barang, ukuran, qty)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan transaksi: {str(e)}")
            return False

    def reset_form(self):
        self.ui.tableWidget_barang.setRowCount(0)
        self.ui.lineEdit_subtotal.setText("Rp 0")
        self.ui.lineEdit_total.setText("Rp 0")
        self.diskon_hari_besar()

    def kembali_dashboard(self):
        self.close()
        if self.parent_window:
            self.parent_window.show()

# ==================== MAIN ====================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = HalamanPenjualanBaru()
    window.show()
    sys.exit(app.exec_())
