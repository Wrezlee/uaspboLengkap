# -*- coding: utf-8 -*-

from form_list_jenis_pakaian import Ui_StokPakaianForm as Ui_ListJenis
import form_kelola as kelola 
# --- TAMBAHAN IMPORT UNTUK LIST USER ---
from form_list_user import Ui_FormListUser as Ui_ListUser 
# ---------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import mysql.connector # Pastikan sudah menginstall library: pip install mysql-connector-python

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 1. SIMPAN REFERENSI MAINWINDOW AGAR BISA DITUTUP NANTI
        self.mainwindow_ref = MainWindow  # <--- TAMBAHAN PENTING
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 983)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # --- TOMBOL MENGELOLA JENIS ---
        self.manageJenisButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageJenisButton.setGeometry(QtCore.QRect(30, 230, 250, 71))
        self.manageJenisButton.setStyleSheet("QPushButton { background-color: #F8BBD0; color: #4A148C; border-radius: 15px; font-weight: bold; font-size: 14px; padding: 8px; border: 2px solid #9C27B0; }\n"
"QPushButton:hover { background-color: #F06292; color: white; }")
        self.manageJenisButton.setObjectName("manageJenisButton")
        
        # =========================================================================
        # KONEKSI TOMBOL PINDAH HALAMAN
        # =========================================================================
        self.manageJenisButton.clicked.connect(self.buka_form_jenis_pakaian)
        # =========================================================================

        self.manageStokButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageStokButton.setGeometry(QtCore.QRect(300, 230, 250, 71))
        self.manageStokButton.setStyleSheet("QPushButton { background-color: #BBDEFB; color: #0D47A1; border-radius: 15px; font-weight: bold; font-size: 14px; padding: 8px; border: 2px solid #1976D2; }\n"
"QPushButton:hover { background-color: #42A5F5; color: white; }")
        self.manageStokButton.setObjectName("manageStokButton")
        
        self.manageUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.manageUserButton.setGeometry(QtCore.QRect(570, 230, 250, 71))
        self.manageUserButton.setStyleSheet("QPushButton { \n"
"      background-color: #FFF9C4; \n"
"      color: #F57F17; \n"
"      border-radius: 15px; \n"
"      font-weight: bold; \n"
"      font-size: 14px; \n"
"      padding: 8px; \n"
"      border: 2px solid #FBC02D; \n"
"}\n"
"QPushButton:hover { \n"
"      background-color: #FBC02D; \n"
"      color: white; \n"
"}")
        self.manageUserButton.setObjectName("manageUserButton")
        # --- TAMBAHAN KONEKSI UNTUK USER ---
        self.manageUserButton.clicked.connect(self.buka_form_user)
        # -----------------------------------
        
        self.viewLaporanButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewLaporanButton.setGeometry(QtCore.QRect(840, 230, 250, 71))
        self.viewLaporanButton.setStyleSheet("QPushButton { background-color: #C8E6C9; color: #1B5E20; border-radius: 15px; font-weight: bold; font-size: 14px; padding: 8px; border: 2px solid #4CAF50; }\n"
"QPushButton:hover { background-color: #66BB6A; color: white; }")
        self.viewLaporanButton.setObjectName("viewLaporanButton")
        
        # --- TAMBAHAN KONEKSI UNTUK LAPORAN KEUANGAN ---
        self.viewLaporanButton.clicked.connect(self.buka_laporan_keuangan)
        # -----------------------------------------------
        
        self.searchPalingLaku = QtWidgets.QLineEdit(self.centralwidget)
        self.searchPalingLaku.setGeometry(QtCore.QRect(30, 310, 1060, 45))
        self.searchPalingLaku.setStyleSheet("QLineEdit {\n"
"      border: 2px solid #FBC02D;\n"
"      border-radius: 10px;\n"
"      padding-left: 15px;\n"
"      font-size: 14px;\n"
"      background-color: #FFFFFF;\n"
"}")
        self.searchPalingLaku.setObjectName("searchPalingLaku")
        # HUBUNGKAN PENCARIAN (REAL-TIME)
        self.searchPalingLaku.textChanged.connect(self.cari_paling_laku)
        
        self.tabelHasilCari = QtWidgets.QTableWidget(self.centralwidget)
        self.tabelHasilCari.setGeometry(QtCore.QRect(30, 360, 1060, 141))
        self.tabelHasilCari.setStyleSheet("\n"
"      QTableWidget {\n"
"       background-color: #FFFFFF;\n"
"       border: 2px solid #FBC02D;\n"
"       border-radius: 10px;\n"
"       gridline-color: #E1BEE7;\n"
"       font-size: 13px;\n"
"      }\n"
"      QHeaderView::section {\n"
"       background-color: #FFF9C4;\n"
"       color: #F57F17;\n"
"       font-weight: bold;\n"
"       border: none;\n"
"       padding: 5px;\n"
"      }\n"
"     ")
        self.tabelHasilCari.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelHasilCari.setAlternatingRowColors(True)
        self.tabelHasilCari.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabelHasilCari.setColumnCount(6)
        self.tabelHasilCari.setObjectName("tabelHasilCari")
        self.tabelHasilCari.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelHasilCari.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelHasilCari.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelHasilCari.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelHasilCari.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelHasilCari.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelHasilCari.setHorizontalHeaderItem(5, item)
        self.tabelHasilCari.horizontalHeader().setVisible(True)
        self.tabelHasilCari.horizontalHeader().setCascadingSectionResizes(True)
        self.tabelHasilCari.horizontalHeader().setDefaultSectionSize(176)
        self.tabelHasilCari.horizontalHeader().setStretchLastSection(True)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 510, 1061, 341))
        self.frame.setStyleSheet("QFrame { background-color: white; border-radius: 20px; border: 3px solid #E1BEE7; padding: 15px; }\n"
"QLabel { background-color: #F3E5F5; color: #4A148C; border-radius: 15px; padding: 10px; font-weight: bold; }")
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 70, 211, 241))
        self.label.setPixmap(QtGui.QPixmap("foto/1.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(300, 70, 211, 241))
        self.label_2.setPixmap(QtGui.QPixmap("foto/3.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(560, 70, 211, 241))
        self.label_3.setPixmap(QtGui.QPixmap("foto/2.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.welcomeSubtitleLabel = QtWidgets.QLabel(self.frame)
        self.welcomeSubtitleLabel.setGeometry(QtCore.QRect(260, 10, 541, 51))
        self.welcomeSubtitleLabel.setStyleSheet("font-size: 16px; color: #757575;")
        self.welcomeSubtitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeSubtitleLabel.setObjectName("welcomeSubtitleLabel")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(810, 70, 211, 241))
        self.label_5.setPixmap(QtGui.QPixmap("foto/4.jpeg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        
        # --- TOMBOL LOGOUT ---
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(460, 870, 200, 45))
        self.logoutButton.setStyleSheet("QPushButton { background-color: #B0BEC5; color: #263238; border-radius: 22px; font-weight: bold; font-size: 14px; padding: 10px 20px; border: 2px solid #78909C; }\n"
"QPushButton:hover { background-color: #78909C; color: white; }")
        self.logoutButton.setObjectName("logoutButton")
        
        # =========================================================================
        # KONEKSI TOMBOL LOGOUT
        # =========================================================================
        self.logoutButton.clicked.connect(self.aksi_logout)
        # =========================================================================

        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(10, 10, 1110, 212))
        self.headerFrame.setStyleSheet("QFrame { background-color: #E1BEE7; border-radius: 20px; padding: 20px; }")
        self.headerFrame.setObjectName("headerFrame")
        self.label_4 = QtWidgets.QLabel(self.headerFrame)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1111, 212))
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/LENOVO/Downloads/Taobao Banner Clothing Background.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.headerFrame)
        self.label_7.setGeometry(QtCore.QRect(40, -10, 1021, 231))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("foto/Background.jpeg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.titleLabel_2 = QtWidgets.QLabel(self.headerFrame)
        self.titleLabel_2.setGeometry(QtCore.QRect(410, 30, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLabel_2.setFont(font)
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.subtitleLabel_2 = QtWidgets.QLabel(self.headerFrame)
        self.subtitleLabel_2.setGeometry(QtCore.QRect(450, 120, 171, 51))
        self.subtitleLabel_2.setObjectName("subtitleLabel_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.manageStokButton.clicked.connect(self.kelola)
        
        # Load data pertama kali saat dibuka
        self.cari_paling_laku()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard Admin"))
        self.manageJenisButton.setText(_translate("MainWindow", "Mengelola Jenis Pakaian 👚"))
        self.manageStokButton.setText(_translate("MainWindow", "Mengelola Stok Pakaian 📦"))
        self.manageUserButton.setText(_translate("MainWindow", "Mengelola User 👥"))
        # TULISAN DIBAWAH INI TELAH DIGANTI
        self.viewLaporanButton.setText(_translate("MainWindow", "Lihat Laporan Keuangan 📊"))
        self.searchPalingLaku.setPlaceholderText(_translate("MainWindow", "🔍 Cari barang paling banyak dijual di sini..."))
        item = self.tabelHasilCari.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nama Barang"))
        item = self.tabelHasilCari.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ukuran"))
        item = self.tabelHasilCari.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Warna"))
        item = self.tabelHasilCari.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Terjual"))
        item = self.tabelHasilCari.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Harga Satuan"))
        item = self.tabelHasilCari.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Subtotal"))
        self.welcomeSubtitleLabel.setText(_translate("MainWindow", "Pilih menu di atas untuk mulai mengelola toko pakaian Anda"))
        self.logoutButton.setText(_translate("MainWindow", "Keluar (Logout) 🚪"))
        self.titleLabel_2.setText(_translate("MainWindow", "Selamat Datang Admin"))
        self.subtitleLabel_2.setText(_translate("MainWindow", "Toko Pakaian Kece ✨"))

    def cari_paling_laku(self):
        text_cari = self.searchPalingLaku.text()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pbo_uas"
            )
            cursor = mydb.cursor()
            query = """
                SELECT nama_barang, ukuran, warna, SUM(qty) as total_qty, harga, SUM(subtotal)
                FROM detail_penjualan 
                WHERE nama_barang LIKE %s 
                GROUP BY nama_barang, ukuran, warna 
                ORDER BY total_qty DESC
            """
            val = ("%" + text_cari + "%",)
            cursor.execute(query, val)
            result = cursor.fetchall()

            self.tabelHasilCari.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tabelHasilCari.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tabelHasilCari.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            
            mydb.close()
        except mysql.connector.Error as err:
            print(f"Error Database: {err}")

    def buka_form_jenis_pakaian(self):
        self.window_jenis = QtWidgets.QWidget() 
        self.ui_jenis = Ui_ListJenis()
        self.ui_jenis.setupUi(self.window_jenis)
        self.window_jenis.show()
        self.mainwindow_ref.close() 

    def buka_form_user(self):
        self.window_user = QtWidgets.QMainWindow() 
        self.ui_user = Ui_ListUser()
        self.ui_user.setupUi(self.window_user)
        self.window_user.show()
        self.mainwindow_ref.close() 

    # --- PERBAIKAN LOGIKA BUKA LAPORAN KEUANGAN ---
    def buka_laporan_keuangan(self):
        try:
            import jajallaporkeu 
            self.window_laporan = QtWidgets.QMainWindow()
            
            # GANTI 'Ui_MainWindow' menjadi 'Ui_FormLaporanKeuangan'
            self.ui_laporan = jajallaporkeu.Ui_FormLaporanKeuangan() 
            
            self.ui_laporan.setupUi(self.window_laporan)
            self.window_laporan.show()
            self.mainwindow_ref.close()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal membuka laporan: {e}")
    # ---------------------------------------------
    
    def kelola(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = kelola.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.centralwidget.window().close()
        self.window.show()

    def aksi_logout(self):
        reply = QMessageBox.question(
            self.mainwindow_ref, 
            "Konfirmasi", 
            "Yakin ingin logout?", 
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                from form_login import LoginWindow 
                self.login_win = LoginWindow()
                self.login_win.show()
                self.mainwindow_ref.close()
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Gagal logout:\n{e}")
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())