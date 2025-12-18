# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from openpyxl import Workbook
from barang import Barang


# ================= DATABASE =================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbo_uas"
    )


# ================= WINDOW =================
class DataStokWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Stok Barang")
        self.resize(900, 677)

        # ===== CENTRAL =====
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setStyleSheet(
            "QWidget { background-color: #E3F2FD; }"
        )

        # ===== TITLE =====
        self.label = QtWidgets.QLabel("DATA STOK BARANG 📦", self.centralwidget)
        self.label.setGeometry(210, 10, 501, 51)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(
            "color: #0D47A1; font: bold 24pt 'Times New Roman';"
        )

        # ===== FILTER =====
        self.groupBox = QtWidgets.QGroupBox("Filter Data", self.centralwidget)
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

        self.label_kat = QtWidgets.QLabel("Jenis:", self.groupBox)
        self.label_kat.setGeometry(30, 35, 80, 25)

        self.comboBox_jenis = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_jenis.setGeometry(120, 35, 200, 30)

        self.btn_refresh = QtWidgets.QPushButton("Refresh Data", self.groupBox)
        self.btn_refresh.setGeometry(650, 35, 120, 30)
        self.btn_refresh.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 6px;
                font: bold 10pt "Times New Roman";
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
        """)

        # ===== TABLE =====
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(50, 180, 800, 400)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID Barang",
            "Jenis",
            "Nama Barang",
            "Ukuran",
            "Stok",
            "Harga"
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #BBDEFB;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                padding: 5px;
            }
        """)

        # ===== EXPORT =====
        self.btn_export = QtWidgets.QPushButton("Export Excel", self.centralwidget)
        self.btn_export.setGeometry(60, 590, 141, 35)
        self.btn_export.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border-radius: 6px;
                font: bold 11pt "Times New Roman";
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)

        # ===== LOGIC =====
        self.load_jenis()
        self.load_data()

        self.btn_refresh.clicked.connect(self.refresh_data)
        self.comboBox_jenis.currentIndexChanged.connect(self.filter)
        self.btn_export.clicked.connect(self.export_excel)

    # ================= LOAD KATEGORI =================
    def load_jenis(self):
        self.comboBox_jenis.clear()
        self.comboBox_jenis.addItem("Semua", None)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_jenis, nama_jenis FROM jenis")
        for id_jenis, nama in cursor.fetchall():
            self.comboBox_jenis.addItem(nama, id_jenis)
        conn.close()

    def filter(self):
        jenis_filter = self.comboBox_jenis.currentText().lower()

        for row in range(self.tableWidget.rowCount()):
            jenis_item = self.tableWidget.item(row, 1)
            jenis_text = jenis_item.text().lower() if jenis_item else ""

            # 🔹 Jika pilih "Semua", tampilkan semua data
            if jenis_filter == "semua":
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, jenis_filter != jenis_text)


    # ================= LOAD DATA =================
    def load_data(self):
        data = Barang.tampil_data()
        self.tableWidget.setRowCount(len(data))

        kolom_center = [0, 3, 4, 5]

        for r, row in enumerate(data):
            for c, val in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(val))
                if c in kolom_center:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(r, c, item)

    # ================= REFRESH =================
    def refresh_data(self):
        self.comboBox_jenis.setCurrentIndex(0)
        QtWidgets.QMessageBox.information(
            self, "Info", "Data berhasil direfresh"
        )
        self.load_data()

    # ================= EXPORT EXCEL =================
    def export_excel(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Simpan File",
            "data_stok.xlsx",
            "Excel Files (*.xlsx)"
        )

        if not path:
            return

        wb = Workbook()
        ws = wb.active
        ws.title = "Data Stok"

        headers = [
            "ID Barang","Jenis", "Nama Barang",
            "Ukuran", "Stok", "Harga"
        ]
        ws.append(headers)

        for row in range(self.tableWidget.rowCount()):
            row_data = []
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                row_data.append(item.text() if item else "")
            ws.append(row_data)

        wb.save(path)

        QtWidgets.QMessageBox.information(
            self, "Sukses", "Data berhasil diexport ke Excel"
        )


# ================= RUN =================
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DataStokWindow()
    window.show()
    sys.exit(app.exec_())
