# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listuser.ui'
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

class Ui_FormListUser(object):
    def setupUi(self, FormListUser):
        self.mainwindow_ref = FormListUser # Simpan referensi window
        FormListUser.setObjectName("FormListUser")
        FormListUser.resize(950, 793) 
        FormListUser.setStyleSheet("\n"
"    QWidget { background-color: #121212; color: #E0E0E0; font-family: 'Segoe UI', sans-serif; font-size: 11pt; }\n"
"    \n"
"    /* CARD */\n"
"    QFrame#card { background-color: #1E1E1E; border: 1px solid #333333; border-radius: 12px; }\n"
"    \n"
"    /* INPUTS */\n"
"    QLineEdit, QComboBox { \n"
"        background-color: #2D2D2D; \n"
"        border: 1px solid #404040; \n"
"        border-radius: 8px; \n"
"        padding: 6px 12px; \n"
"        color: white; \n"
"    }\n"
"    QLineEdit:focus, QComboBox:focus { border: 2px solid #2962FF; }\n"
"\n"
"    /* TABLE - TEKS BIRU TUA */\n"
"    QTableWidget { background-color: #1E1E1E; border: 1px solid #333333; gridline-color: #2C2C2C; border-radius: 8px; color: #0D47A1; }\n"
"    QHeaderView::section { background-color: #252525; padding: 8px; border: none; border-bottom: 2px solid #2962FF; color: white; font-weight: bold; }\n"
"    \n"
"    /* BUTTONS */\n"
"    QPushButton { background-color: #333333; border: 1px solid #444444; border-radius: 8px; padding: 10px; color: white; font-weight: bold; }\n"
"    QPushButton:hover { background-color: #424242; }\n"
"    \n"
"    /* ACTION BUTTONS */\n"
"    QPushButton#btnTambah, QPushButton#btnUpdate { background-color: #2962FF; border: none; }\n"
"    QPushButton#btnTambah:hover, QPushButton#btnUpdate:hover { background-color: #1565C0; }\n"
"    QPushButton#btnHapus { background-color: #D32F2F; border: none; }\n"
"    QPushButton#btnHapus:hover { background-color: #B71C1C; }\n"
"    QPushButton#btnKeluar { background-color: #455A64; border: none; }\n"
"    QPushButton#btnKeluar:hover { background-color: #263238; }\n"
"    \n"
"    /* SEARCH BUTTON */\n"
"    QPushButton#btnCari { background-color: #2D2D2D; padding: 6px 12px; }\n"
"    QPushButton#btnCari:hover { background-color: #383838; }\n"
"   ")
        self.centralwidget = QtWidgets.QWidget(FormListUser)
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
        self.filterLayout.setContentsMargins(-1, -1, -1, 10)
        self.filterLayout.setObjectName("filterLayout")
        self.lineEdit_search = QtWidgets.QLineEdit(self.card)
        self.lineEdit_search.setMinimumSize(QtCore.QSize(250, 35))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.filterLayout.addWidget(self.lineEdit_search)
        self.comboBox_filterLevel = QtWidgets.QComboBox(self.card)
        self.comboBox_filterLevel.setMinimumSize(QtCore.QSize(150, 35))
        self.comboBox_filterLevel.setObjectName("comboBox_filterLevel")
        self.comboBox_filterLevel.addItem("")
        self.comboBox_filterLevel.addItem("")
        self.comboBox_filterLevel.addItem("")
        self.filterLayout.addWidget(self.comboBox_filterLevel)
        self.btnCari = QtWidgets.QPushButton(self.card)
        self.btnCari.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCari.setObjectName("btnCari")
        self.filterLayout.addWidget(self.btnCari)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.filterLayout.addItem(spacerItem)
        self.cardLayout.addLayout(self.filterLayout)
        self.tableUser = QtWidgets.QTableWidget(self.card)
        self.tableUser.setAlternatingRowColors(True)
        self.tableUser.setColumnCount(5)
        self.tableUser.setObjectName("tableUser")
        self.tableUser.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(4, item)
        self.tableUser.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.cardLayout.addWidget(self.tableUser)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.btnTambah = QtWidgets.QPushButton(self.card)
        self.btnTambah.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTambah.setObjectName("btnTambah")
        self.buttonLayout.addWidget(self.btnTambah)
        self.btnUpdate = QtWidgets.QPushButton(self.card)
        self.btnUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUpdate.setObjectName("btnUpdate")
        self.buttonLayout.addWidget(self.btnUpdate)
        self.btnHapus = QtWidgets.QPushButton(self.card)
        self.btnHapus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHapus.setObjectName("btnHapus")
        self.buttonLayout.addWidget(self.btnHapus)
        
        # --- TOMBOL KELUAR ---
        self.btnKeluar = QtWidgets.QPushButton(self.card)
        self.btnKeluar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnKeluar.setObjectName("btnKeluar")
        self.btnKeluar.setText("⬅ Keluar")
        self.buttonLayout.addWidget(self.btnKeluar)
        
        self.cardLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.card)
        FormListUser.setCentralWidget(self.centralwidget)

        self.retranslateUi(FormListUser)
        QtCore.QMetaObject.connectSlotsByName(FormListUser)

        # --- KONEKSI TOMBOL & LOAD DATA ---
        self.btnCari.clicked.connect(self.load_data)
        self.btnTambah.clicked.connect(self.open_tambah)
        self.btnUpdate.clicked.connect(self.open_update)
        self.btnHapus.clicked.connect(self.open_hapus)
        self.btnKeluar.clicked.connect(self.aksi_keluar)
        self.load_data(is_initial=True) 

    def retranslateUi(self, FormListUser):
        _translate = QtCore.QCoreApplication.translate
        FormListUser.setWindowTitle(_translate("FormListUser", "Daftar User"))
        self.label.setStyleSheet(_translate("FormListUser", "font-size: 18pt; font-weight: bold; color: white; margin-bottom: 10px;"))
        self.label.setText(_translate("FormListUser", "👤 Manajemen User"))
        self.lineEdit_search.setPlaceholderText(_translate("FormListUser", "🔍 Cari Nama atau Username..."))
        self.comboBox_filterLevel.setItemText(0, _translate("FormListUser", "Semua Level"))
        self.comboBox_filterLevel.setItemText(1, _translate("FormListUser", "Admin"))
        self.comboBox_filterLevel.setItemText(2, _translate("FormListUser", "Kasir"))
        self.btnCari.setText(_translate("FormListUser", "Cari"))
        item = self.tableUser.horizontalHeaderItem(0)
        item.setText(_translate("FormListUser", "ID"))
        item = self.tableUser.horizontalHeaderItem(1)
        item.setText(_translate("FormListUser", "Nama Lengkap"))
        item = self.tableUser.horizontalHeaderItem(2)
        item.setText(_translate("FormListUser", "Username"))
        item = self.tableUser.horizontalHeaderItem(3)
        item.setText(_translate("FormListUser", "Level"))
        item = self.tableUser.horizontalHeaderItem(4)
        item.setText(_translate("FormListUser", "Password"))
        self.btnTambah.setText(_translate("FormListUser", "+ Tambah User"))
        self.btnUpdate.setText(_translate("FormListUser", "✎ Update User"))
        self.btnHapus.setText(_translate("FormListUser", "🗑 Hapus User"))

    def load_data(self, is_initial=False):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pbo_uas")
            cursor = mydb.cursor()
            search_text = self.lineEdit_search.text()
            level_filter = self.comboBox_filterLevel.currentText()
            
            query = "SELECT username, password, nama_lengkap, level FROM users WHERE 1=1"
            params = []
            
            if search_text:
                query += " AND (nama_lengkap LIKE %s OR username LIKE %s)"
                params.extend([f"%{search_text}%", f"%{search_text}%"])
            
            if level_filter != "Semua Level":
                query += " AND level = %s"
                params.append(level_filter.lower())
                
            cursor.execute(query, params)
            result = cursor.fetchall()
            
            # --- LOGIKA PENGECEKAN DATA ---
            if not result and not is_initial:
                QMessageBox.information(None, "Hasil Pencarian", "Data tidak ditemukan.")
            
            self.tableUser.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableUser.insertRow(row_number)
                # Urutan: ID, Nama, Username, Level, Password
                data_list = [row_number+1, row_data[2], row_data[0], row_data[3], row_data[1]]
                for col_idx, val in enumerate(data_list):
                    item = QTableWidgetItem(str(val))
                    item.setForeground(QtGui.QColor("#0D47A1")) # Biru Tua
                    self.tableUser.setItem(row_number, col_idx, item)
            mydb.close()
        except mysql.connector.Error as err:
            print(f"Error Database: {err}")

    def open_tambah(self):
        try:
            # Local Import untuk mencegah Circular Import
            from createuser_fix import Ui_FormTambahUser
            self.window_tambah = QtWidgets.QWidget()
            self.ui_tambah = Ui_FormTambahUser()
            self.ui_tambah.setupUi(self.window_tambah)
            self.window_tambah.show()
            self.mainwindow_ref.close()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal membuka form Tambah:\n{e}")

    def open_update(self):
        try:
            from updateuser import Ui_FormUpdateUser
            self.window_update = QtWidgets.QWidget()
            self.ui_update = Ui_FormUpdateUser()
            self.ui_update.setupUi(self.window_update)
            self.window_update.show()
            self.mainwindow_ref.close()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal membuka form Update:\n{e}")

    def open_hapus(self):
        try:
            from hapususer import Ui_FormHapusUser
            self.window_hapus = QtWidgets.QWidget()
            self.ui_hapus = Ui_FormHapusUser()
            self.ui_hapus.setupUi(self.window_hapus)
            self.window_hapus.show()
            self.mainwindow_ref.close()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal membuka form Hapus:\n{e}")

    def aksi_keluar(self):
        try:
            from form_dashboard_admin import Ui_MainWindow as Ui_Dashboard
            self.window_dash = QtWidgets.QMainWindow()
            self.ui_dash = Ui_Dashboard()
            self.ui_dash.setupUi(self.window_dash)
            self.window_dash.show()
            self.mainwindow_ref.close()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal kembali ke Dashboard:\n{e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormListUser = QtWidgets.QMainWindow()
    ui = Ui_FormListUser()
    ui.setupUi(FormListUser)
    FormListUser.show()
    sys.exit(app.exec_())