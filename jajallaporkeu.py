# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jajallaporkeu.ui'
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbo_uas"
    )

class Ui_FormLaporanKeuangan(object):
    def setupUi(self, FormLaporanKeuangan):
        FormLaporanKeuangan.setObjectName("FormLaporanKeuangan")
        FormLaporanKeuangan.resize(900, 762)
        FormLaporanKeuangan.setStyleSheet("\n"
"    QWidget { background-color: #121212; color: #FFFFFF; font-family: 'Segoe UI', sans-serif; font-size: 11pt; }\n"
"    \n"
"    /* CARD STYLE */\n"
"    QFrame#card { background-color: #1E1E1E; border-radius: 12px; border: 1px solid #333333; }\n"
"    \n"
"    /* INPUT STYLE */\n"
"    QLineEdit, QDateEdit { \n"
"        background-color: #2D2D2D; \n"
"        border: 1px solid #404040; \n"
"        border-radius: 8px; \n"
"        padding: 6px 12px; \n"
"        color: white; \n"
"        min-height: 20px;\n"
"    }\n"
"    QLineEdit:focus, QDateEdit:focus { border: 2px solid #00E676; }\n"
"    \n"
"    /* TABLE STYLE */\n"
"    QTableWidget { background-color: #1E1E1E; border: 1px solid #333333; gridline-color: #2C2C2C; border-radius: 8px; }\n"
"    QHeaderView::section { background-color: #252525; padding: 10px; border: none; border-bottom: 2px solid #00E676; font-weight: bold; color: white; }\n"
"    \n"
"    /* LABEL & TEXT */\n"
"    QLabel { font-weight: bold; color: #E0E0E0; }\n"
"    \n"
"    /* BUTTON STYLE */\n"
"    QPushButton { \n"
"        background-color: #2D2D2D; \n"
"        border: 1px solid #404040; \n"
"        border-radius: 8px; \n"
"        padding: 8px 16px; \n"
"        color: white; \n"
"        font-weight: bold; \n"
"    }\n"
"    QPushButton:hover { background-color: #383838; }\n"
"    \n"
"    /* Filter Button (Green) */\n"
"    QPushButton#btnFilter { \n"
"        background-color: #00E676; \n"
"        color: #121212; \n"
"        border: none; \n"
"    }\n"
"    QPushButton#btnFilter:hover { background-color: #00C853; }\n"
"\n"
"QPushButton#btnRefresh { \n"
"        background-color: #00E676; \n"
"        color: #121212; \n"
"        border: none; \n"
"    }\n"
"    QPushButton#btnFilter:hover { background-color: #00C853; }\n"
"\n"
"    /* Back Button (Red) */\n"
"    QPushButton#btnKembali {\n"
"        background-color: #D32F2F;\n"
"        color: white;\n"
"        border: none;\n"
"        padding: 10px 20px;\n"
"    }\n"
"    QPushButton#btnKembali:hover { background-color: #B71C1C; }\n"
"   ")
        self.centralwidget = QtWidgets.QWidget(FormLaporanKeuangan)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.card = QtWidgets.QFrame(self.centralwidget)
        self.card.setObjectName("card")
        self.cardLayout = QtWidgets.QVBoxLayout(self.card)
        self.cardLayout.setObjectName("cardLayout")
        self.label = QtWidgets.QLabel(self.card)
        self.label.setObjectName("label")
        self.cardLayout.addWidget(self.label)
        self.filterLayout = QtWidgets.QHBoxLayout()
        self.filterLayout.setContentsMargins(-1, 0, -1, 10)
        self.filterLayout.setObjectName("filterLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.filterLayout.addItem(spacerItem)
        self.label_dari = QtWidgets.QLabel(self.card)
        self.label_dari.setObjectName("label_dari")
        self.filterLayout.addWidget(self.label_dari)
        self.dateEdit_start = QtWidgets.QDateEdit(self.card)
        self.dateEdit_start.setCalendarPopup(True)
        self.dateEdit_start.setDate(QtCore.QDate(2024, 1, 1))
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.filterLayout.addWidget(self.dateEdit_start)
        self.label_sampai = QtWidgets.QLabel(self.card)
        self.label_sampai.setObjectName("label_sampai")
        self.filterLayout.addWidget(self.label_sampai)
        self.dateEdit_end = QtWidgets.QDateEdit(self.card)
        self.dateEdit_end.setCalendarPopup(True)
        self.dateEdit_end.setDate(QtCore.QDate(2024, 12, 31))
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.filterLayout.addWidget(self.dateEdit_end)
        self.btnFilter = QtWidgets.QPushButton(self.card)
        self.btnFilter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btnFilter.setIcon(icon)
        self.btnFilter.setObjectName("btnFilter")
        self.filterLayout.addWidget(self.btnFilter)
        self.btnRefresh = QtWidgets.QPushButton(self.card)
        self.btnRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setObjectName("btnRefresh")
        self.filterLayout.addWidget(self.btnRefresh)
        self.cardLayout.addLayout(self.filterLayout)
        self.tableLaporan = QtWidgets.QTableWidget(self.card)
        self.tableLaporan.setAlternatingRowColors(False)
        self.tableLaporan.setColumnCount(2)
        self.tableLaporan.setObjectName("tableLaporan")
        self.tableLaporan.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableLaporan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLaporan.setHorizontalHeaderItem(1, item)
        self.cardLayout.addWidget(self.tableLaporan)
        self.mainLayout.addWidget(self.card)
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.setObjectName("bottomLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem1)
        self.btnKembali = QtWidgets.QPushButton(self.centralwidget)
        self.btnKembali.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnKembali.setObjectName("btnKembali")
        self.bottomLayout.addWidget(self.btnKembali)
        self.mainLayout.addLayout(self.bottomLayout)
        self.label_total = QtWidgets.QLabel("Total Penjualan: Rp 0",
        self.centralwidget)
        self.label_total.setGeometry(50, 690, 400, 30)
        self.label_total.setStyleSheet(
            "color: #D32F2F; font: bold 14pt 'Times New Roman';"
        )
        FormLaporanKeuangan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormLaporanKeuangan)
        self.statusbar.setObjectName("statusbar")
        FormLaporanKeuangan.setStatusBar(self.statusbar)
        
        # --- KONEKSI LOGIKA ---
        self.load_data()
        self.btnFilter.clicked.connect(self.filter_data)
        self.btnRefresh.clicked.connect(self.load_data)
        self.btnKembali.clicked.connect(self.aksi_kembali) # <--- TAMBAHAN KONEKSI TOMBOL

        self.retranslateUi(FormLaporanKeuangan)
        QtCore.QMetaObject.connectSlotsByName(FormLaporanKeuangan)

    def retranslateUi(self, FormLaporanKeuangan):
        _translate = QtCore.QCoreApplication.translate
        FormLaporanKeuangan.setWindowTitle(_translate("FormLaporanKeuangan", "Laporan Keuangan"))
        self.label.setStyleSheet(_translate("FormLaporanKeuangan", "font-size: 18pt; margin-bottom: 10px; color: #00E676;"))
        self.label.setText(_translate("FormLaporanKeuangan", "📄 Tabel Laporan Keuangan"))
        self.label_dari.setText(_translate("FormLaporanKeuangan", "Dari:"))
        self.dateEdit_start.setDisplayFormat(_translate("FormLaporanKeuangan", "dd/MM/yyyy"))
        self.label_sampai.setText(_translate("FormLaporanKeuangan", "Sampai:"))
        self.dateEdit_end.setDisplayFormat(_translate("FormLaporanKeuangan", "dd/MM/yyyy"))
        self.btnFilter.setText(_translate("FormLaporanKeuangan", "Tampilkan"))
        self.btnRefresh.setText(_translate("FormLaporanKeuangan", "Refresh"))
        item = self.tableLaporan.horizontalHeaderItem(0)
        item.setText(_translate("FormLaporanKeuangan", "Tanggal"))
        item = self.tableLaporan.horizontalHeaderItem(1)
        item.setText(_translate("FormLaporanKeuangan", "Pendapatan"))
        self.btnKembali.setText(_translate("FormLaporanKeuangan", "Kembali"))

    # --- TAMBAHAN LOGIKA KEMBALI KE DASHBOARD ---
    def aksi_kembali(self):
        try:
            # Menggunakan local import di dalam fungsi untuk memutus circular import
            from form_dashboard_admin import Ui_MainWindow as Ui_Dashboard
            self.window_dash = QtWidgets.QMainWindow()
            self.ui_dash = Ui_Dashboard()
            self.ui_dash.setupUi(self.window_dash)
            self.window_dash.show()
            # Menutup jendela laporan keuangan saat ini
            self.centralwidget.window().close() 
        except Exception as e:
            print(f"Gagal kembali ke dashboard: {e}")
    # --------------------------------------------

    def load_data(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT 
                tanggal,
                total
            FROM penjualan
            """
        cursor.execute(query)
        data = cursor.fetchall()
        self.tableLaporan.setRowCount(len(data))
        total_penjualan = 0

        for row, record in enumerate(data):
            for col, value in enumerate(record):
                self.tableLaporan.setItem(
                    row, col,
                    QtWidgets.QTableWidgetItem(str(value))
                )
            total_penjualan += int(record[1])

        self.label_total.setText(
            f"Total Penjualan: Rp {total_penjualan:,}"
        )

        conn.close()

    def filter_data(self):
        start_date = self.dateEdit_start.date().toString("yyyy-MM-dd")
        end_date = self.dateEdit_end.date().toString("yyyy-MM-dd")

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT tanggal, total
            FROM penjualan
            WHERE tanggal BETWEEN %s AND %s
            ORDER BY tanggal ASC
        """

        cursor.execute(query, (start_date, end_date))
        data = cursor.fetchall()

        self.tableLaporan.setRowCount(len(data))
        total_penjualan = 0

        for row, record in enumerate(data):
            self.tableLaporan.setItem(
                row, 0,
                QtWidgets.QTableWidgetItem(str(record[0]))
            )
            self.tableLaporan.setItem(
                row, 1,
                QtWidgets.QTableWidgetItem(f"{record[1]:,}")
            )
            total_penjualan += int(record[1])

        self.label_total.setText(
            f"Total Penjualan: Rp {total_penjualan:,}"
        )

        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormLaporanKeuangan = QtWidgets.QMainWindow()
    ui = Ui_FormLaporanKeuangan()
    ui.setupUi(FormLaporanKeuangan)
    FormLaporanKeuangan.show()
    sys.exit(app.exec_())