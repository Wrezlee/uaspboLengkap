# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from datetime import datetime


# ================= DATABASE =================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbo_uas"
    )


# ================= WINDOW =================
class RiwayatTransaksiWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Riwayat Transaksi")
        self.resize(900, 700)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setStyleSheet(
            "QWidget { background-color: #E3F2FD; }"
        )

        # ===== TITLE =====
        self.label = QtWidgets.QLabel("RIWAYAT TRANSAKSI 📊", self.centralwidget)
        self.label.setGeometry(200, 20, 501, 51)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(
            "color: #0D47A1; font: bold 24pt 'Times New Roman';"
        )

        # ===== FILTER =====
        self.groupBox = QtWidgets.QGroupBox("Filter Periode", self.centralwidget)
        self.groupBox.setGeometry(50, 80, 800, 80)
        self.groupBox.setStyleSheet("""
            QGroupBox {
                background-color: white;
                border: 2px solid #BBDEFB;
                border-radius: 10px;
                font: bold 12pt "Times New Roman";
                color: #1976D2;
            }
        """)

        self.lbl_bulan = QtWidgets.QLabel("Bulan:", self.groupBox)
        self.lbl_bulan.setGeometry(30, 35, 50, 25)

        self.comboBox_bulan = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_bulan.setGeometry(90, 35, 150, 30)

        self.lbl_tahun = QtWidgets.QLabel("Tahun:", self.groupBox)
        self.lbl_tahun.setGeometry(260, 35, 50, 25)

        self.comboBox_tahun = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_tahun.setGeometry(320, 35, 100, 30)

        self.btn_tampil = QtWidgets.QPushButton("Tampilkan", self.groupBox)
        self.btn_tampil.setGeometry(450, 35, 100, 30)
        self.btn_tampil.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 6px;
                font: bold 10pt "Times New Roman";
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)

        # ===== TABLE =====
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(50, 180, 800, 400)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels([
            "Tanggal",
            "Nama Barang",
            "Qty",
            "Harga",
            "Subtotal",
            "ID Penjualan"
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )

        # ===== TOTAL =====
        self.label_total = QtWidgets.QLabel(
            "Total Penjualan: Rp 0", self.centralwidget
        )
        self.label_total.setGeometry(50, 590, 400, 30)
        self.label_total.setStyleSheet(
            "color: #D32F2F; font: bold 14pt 'Times New Roman';"
        )

        # ===== LOGIC =====
        self.load_bulan()
        self.load_tahun()
        self.btn_tampil.clicked.connect(self.load_data)

    # ================= BULAN =================
    def load_bulan(self):
        bulan = [
            "Semua",
            "Januari", "Februari", "Maret", "April",
            "Mei", "Juni", "Juli", "Agustus",
            "September", "Oktober", "November", "Desember"
        ]
        self.comboBox_bulan.addItems(bulan)

    # ================= TAHUN =================
    def load_tahun(self):
        tahun_sekarang = datetime.now().year
        for t in range(tahun_sekarang - 5, tahun_sekarang + 1):
            self.comboBox_tahun.addItem(str(t))
        self.comboBox_tahun.setCurrentText(str(tahun_sekarang))

    # ================= LOAD DATA =================
    def load_data(self):
        bulan = self.comboBox_bulan.currentIndex()
        tahun = self.comboBox_tahun.currentText()

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT 
                p.tanggal,
                d.nama_barang,
                d.qty,
                d.harga,
                d.subtotal,
                p.no_faktur
            FROM penjualan p
            JOIN detail_penjualan d 
                ON p.no_faktur = d.id_penjualan
            WHERE YEAR(p.tanggal) = %s
            """
        params = [tahun]

        if bulan != 0:
            query += " AND MONTH(p.tanggal) = %s"
            params.append(bulan)

        cursor.execute(query, params)
        data = cursor.fetchall()

        self.tableWidget.setRowCount(len(data))
        total_penjualan = 0

        for row, record in enumerate(data):
            for col, value in enumerate(record):
                self.tableWidget.setItem(
                    row, col,
                    QtWidgets.QTableWidgetItem(str(value))
                )
            total_penjualan += int(record[4])

        self.label_total.setText(
            f"Total Penjualan: Rp {total_penjualan:,}"
        )

        conn.close()


# ================= RUN =================
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = RiwayatTransaksiWindow()
    window.show()
    sys.exit(app.exec_())
