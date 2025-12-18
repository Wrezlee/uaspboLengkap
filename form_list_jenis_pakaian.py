# -*- coding: utf-8 -*-

import sys

# --- IMPORT FILE DATABASE ANDA ---
try:
    from barang import Barang
    from jenis import Jenis 
    from ukuran import Ukuran 
except ImportError:
    print("Pastikan file barang.py, jenis.py, dan ukuran.py ada dalam satu folder.")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


class Ui_StokPakaianForm(object):
    def setupUi(self, StokPakaianForm):
        self.main_form = StokPakaianForm  # Simpan referensi form utama
        StokPakaianForm.setObjectName("StokPakaianForm")
        StokPakaianForm.resize(1250, 900)
        StokPakaianForm.setStyleSheet("/* Background similar to React component */\n"
"QWidget#StokPakaianForm {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #F3E5F5,   /* light lavender */\n"
"        stop:0.5 #E1BEE7, /* soft violet */\n"
"        stop:1 #D7B4EB    /* violet pastel */\n"
"    );\n"
"}\n"
"\n"
"QFrame#headerFrame {\n"
"    background-color: white;\n"
"    border: 4px solid #90CAF9;\n"
"    border-radius: 20px;\n"
"    padding: 15px;\n"
"}\n"
"QFrame#filterFrame {\n"
"    background-color: white;\n"
"    border: 4px solid #CE93D8;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton#backButton {\n"
"    background-color: #EF5350;\n"
"    color: white;\n"
"    border-radius: 12px;\n"
"    padding: 10px 30px; \n"
"    font-size: 18px; \n"
"    font-weight: bold;\n"
"    border: none;\n"
"    min-width: 150px;\n"
"}\n"
"QPushButton#backButton:hover {\n"
"    background-color: #E53935;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border: 2px solid #E0E0E0;\n"
"    border-radius: 10px;\n"
"    gridline-color: #E0E0E0;\n"
"    alternate-background-color: #E3F3FF;\n"
"}\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"}")
        self.headerFrame = QtWidgets.QFrame(StokPakaianForm)
        self.headerFrame.setGeometry(QtCore.QRect(20, 20, 1211, 140))
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.iconLabel = QtWidgets.QLabel(self.headerFrame)
        self.iconLabel.setGeometry(QtCore.QRect(360, 20, 80, 80))
        self.iconLabel.setMinimumSize(QtCore.QSize(80, 80))
        self.iconLabel.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.iconLabel.setFont(font)
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setObjectName("iconLabel")
        self.titleLabel = QtWidgets.QLabel(self.headerFrame)
        self.titleLabel.setGeometry(QtCore.QRect(470, 40, 441, 48))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: #1976D2;")
        self.titleLabel.setObjectName("titleLabel")
        self.filterFrame = QtWidgets.QFrame(StokPakaianForm)
        self.filterFrame.setGeometry(QtCore.QRect(20, 175, 761, 64))
        self.filterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filterFrame.setObjectName("filterFrame")
        self.searchIconLabel = QtWidgets.QLabel(self.filterFrame)
        self.searchIconLabel.setGeometry(QtCore.QRect(15, 15, 28, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchIconLabel.setFont(font)
        self.searchIconLabel.setObjectName("searchIconLabel")
        self.searchTermLineEdit = QtWidgets.QLineEdit(self.filterFrame)
        self.searchTermLineEdit.setGeometry(QtCore.QRect(50, 15, 461, 34))
        self.searchTermLineEdit.setStyleSheet("QLineEdit { border: 2px solid #CE93D8; border-radius: 8px; padding: 5px; } QLineEdit:focus { border: 2px solid #9C27B0; }")
        self.searchTermLineEdit.setObjectName("searchTermLineEdit")
        self.filterIconLabel = QtWidgets.QLabel(self.filterFrame)
        self.filterIconLabel.setGeometry(QtCore.QRect(530, 18, 28, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filterIconLabel.setFont(font)
        self.filterIconLabel.setObjectName("filterIconLabel")
        self.filterKategoriComboBox = QtWidgets.QComboBox(self.filterFrame)
        self.filterKategoriComboBox.setGeometry(QtCore.QRect(570, 20, 171, 32))
        self.filterKategoriComboBox.setStyleSheet("QComboBox { border: 2px solid #CE93D8; border-radius: 8px; padding: 5px; }")
        self.filterKategoriComboBox.setObjectName("filterKategoriComboBox")
        self.filterKategoriComboBox.addItem("")
        self.stokTableWidget = QtWidgets.QTableWidget(StokPakaianForm)
        self.stokTableWidget.setGeometry(QtCore.QRect(20, 254, 761, 581))
        self.stokTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.stokTableWidget.setAlternatingRowColors(True)
        self.stokTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.stokTableWidget.setColumnCount(6)
        self.stokTableWidget.setObjectName("stokTableWidget")
        self.stokTableWidget.setRowCount(0)
        
        headers = ["ID Pakaian", "Jenis", "Nama Barang", "Ukuran", "Stok", "Harga"]
        for i, h in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            item.setText(h)
            self.stokTableWidget.setHorizontalHeaderItem(i, item)
            
        self.stokTableWidget.horizontalHeader().setVisible(True)
        self.stokTableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.stokTableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.stokTableWidget.verticalHeader().setVisible(False)
        self.stokTableWidget.verticalHeader().setDefaultSectionSize(40)
        self.backButton = QtWidgets.QPushButton(StokPakaianForm)
        self.backButton.setGeometry(QtCore.QRect(510, 850, 210, 40))
        self.backButton.setObjectName("backButton")
        self.footerButtonFrame = QtWidgets.QFrame(StokPakaianForm)
        self.footerButtonFrame.setGeometry(QtCore.QRect(20, 816, 326, 64))
        self.footerButtonFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footerButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footerButtonFrame.setObjectName("footerButtonFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.footerButtonFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(StokPakaianForm)
        self.tabWidget.setGeometry(QtCore.QRect(810, 180, 421, 661))
        
        # Stylesheet TabWidget
        self.tabWidget.setStyleSheet("QTabWidget::pane { border: 2px solid #90CAF9; border-radius: 10px; padding: 1px; background-color: #E3F2FD; } QTabWidget::tab-bar { left: 5px; } QTabBar::tab { background: #BBDEFB; border: 1px solid #90CAF9; border-bottom-color: #90CAF9; border-top-left-radius: 8px; border-top-right-radius: 8px; padding: 8px 15px; min-width: 80px; font-weight: bold; color: #1976D2; } QTabBar::tab:selected, QTabBar::tab:hover { background: white; border-color: #90CAF9; border-bottom-color: white; } QGroupBox { background-color: white; border: 2px solid #BBDEFB; border-radius: 10px; margin-top: 10px; padding-top: 20px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top center; padding: 0 10px; color: rgba(0, 0, 0, 180); font: 600 14pt \"Inter\"; } QLineEdit, QComboBox, QSpinBox { border: 1px solid #BBDEFB; border-radius: 6px; padding: 8px; color: rgba(0, 0, 0, 180); } QLineEdit:focus, QComboBox:focus { border: 2px solid #9C27B0; } QTabWidget QPushButton { border: none; border-radius: 8px; padding: 10px; font: 600 11pt \"Inter\"; color: white; min-height: 30px; } QPushButton#pushButton_simpan, QPushButton#pushButton_update { background-color: #4CAF50; } QPushButton#pushButton_simpan:hover, QPushButton#pushButton_update:hover { background-color: #388E3C; } QPushButton#pushButton_hapus, QPushButton#pushButton_kembali, QPushButton#pushButton_cancel, QPushButton#pushButton_cancel1, QPushButton#pushButton_cancel2 { background-color: #F44336; } QPushButton#pushButton_hapus:hover, QPushButton#pushButton_kembali:hover, QPushButton#pushButton_cancel:hover { background-color: #D32F2F; } QPushButton#pushButton_cari_pakaian, QPushButton#pushButton_cari_edit { background-color: #BBDEFB; color: black; font: 500 10pt \"Inter\"; min-height: 10px; padding: 0px; } QPushButton#pushButton_cari_pakaian:hover, QPushButton#pushButton_cari_edit:hover { background-color: #90CAF9; }")
        self.tabWidget.setObjectName("tabWidget")
        
        # --- TAB TAMBAH ---
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_tambah_pakaian = QtWidgets.QGroupBox(self.tab)
        self.groupBox_tambah_pakaian.setGeometry(QtCore.QRect(15, 10, 380, 591))
        self.groupBox_tambah_pakaian.setObjectName("groupBox_tambah_pakaian")
        self.label_id_pakaian = QtWidgets.QLabel(self.groupBox_tambah_pakaian)
        self.label_id_pakaian.setGeometry(QtCore.QRect(12, 28, 97, 21))
        self.label_id_pakaian.setObjectName("label_id_pakaian")
        self.lineEdit_id_pakaian = QtWidgets.QLineEdit(self.groupBox_tambah_pakaian)
        self.lineEdit_id_pakaian.setGeometry(QtCore.QRect(12, 64, 356, 31))
        self.lineEdit_id_pakaian.setObjectName("lineEdit_id_pakaian")
        
        self.label_jenis = QtWidgets.QLabel(self.groupBox_tambah_pakaian)
        self.label_jenis.setGeometry(QtCore.QRect(12, 110, 49, 21))
        self.label_jenis.setObjectName("label_jenis")
        
        self.cmb_jenis = QtWidgets.QComboBox(self.groupBox_tambah_pakaian)
        self.cmb_jenis.setGeometry(QtCore.QRect(12, 146, 356, 31))
        self.cmb_jenis.setObjectName("cmb_jenis")
        
        self.label_nama_barang = QtWidgets.QLabel(self.groupBox_tambah_pakaian)
        self.label_nama_barang.setGeometry(QtCore.QRect(12, 192, 118, 21))
        self.label_nama_barang.setObjectName("label_nama_barang")
        self.lineEdit_nama_barang = QtWidgets.QLineEdit(self.groupBox_tambah_pakaian)
        self.lineEdit_nama_barang.setGeometry(QtCore.QRect(12, 228, 356, 31))
        self.lineEdit_nama_barang.setObjectName("lineEdit_nama_barang")
        
        self.label_ukuran = QtWidgets.QLabel(self.groupBox_tambah_pakaian)
        self.label_ukuran.setGeometry(QtCore.QRect(12, 274, 65, 21))
        self.label_ukuran.setObjectName("label_ukuran")
        
        self.cmb_ukuran = QtWidgets.QComboBox(self.groupBox_tambah_pakaian)
        self.cmb_ukuran.setGeometry(QtCore.QRect(12, 310, 356, 31))
        self.cmb_ukuran.setObjectName("cmb_ukuran")
        
        self.label_stok = QtWidgets.QLabel(self.groupBox_tambah_pakaian)
        self.label_stok.setGeometry(QtCore.QRect(12, 356, 43, 21))
        self.label_stok.setObjectName("label_stok")
        self.lineEdit_stok = QtWidgets.QLineEdit(self.groupBox_tambah_pakaian)
        self.lineEdit_stok.setGeometry(QtCore.QRect(12, 392, 356, 32))
        self.lineEdit_stok.setObjectName("lineEdit_stok")
        self.label_harga = QtWidgets.QLabel(self.groupBox_tambah_pakaian)
        self.label_harga.setGeometry(QtCore.QRect(12, 438, 43, 21))
        self.label_harga.setObjectName("label_harga")
        self.lineEdit_harga = QtWidgets.QLineEdit(self.groupBox_tambah_pakaian)
        self.lineEdit_harga.setGeometry(QtCore.QRect(12, 474, 230, 31))
        self.lineEdit_harga.setObjectName("lineEdit_harga")
        self.pushButton_simpan = QtWidgets.QPushButton(self.groupBox_tambah_pakaian)
        self.pushButton_simpan.setGeometry(QtCore.QRect(70, 530, 111, 50))
        self.pushButton_simpan.setObjectName("pushButton_simpan")
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox_tambah_pakaian)
        self.pushButton_cancel.setGeometry(QtCore.QRect(198, 530, 111, 50))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        
        self.tabWidget.addTab(self.tab, "Tambah")
        
        # --- TAB EDIT ---
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_edit_pakaian = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_edit_pakaian.setGeometry(QtCore.QRect(15, 10, 380, 591))
        self.groupBox_edit_pakaian.setObjectName("groupBox_edit_pakaian")
        self.label_id_pakaian_edit = QtWidgets.QLabel(self.groupBox_edit_pakaian)
        self.label_id_pakaian_edit.setGeometry(QtCore.QRect(12, 28, 97, 21))
        self.label_id_pakaian_edit.setObjectName("label_id_pakaian_edit")
        self.lineEdit_id_pakaian_edit = QtWidgets.QLineEdit(self.groupBox_edit_pakaian)
        self.lineEdit_id_pakaian_edit.setGeometry(QtCore.QRect(12, 64, 271, 31))
        self.lineEdit_id_pakaian_edit.setObjectName("lineEdit_id_pakaian_edit")
        self.pushButton_cari_edit = QtWidgets.QPushButton(self.groupBox_edit_pakaian)
        self.pushButton_cari_edit.setGeometry(QtCore.QRect(295, 64, 63, 50))
        self.pushButton_cari_edit.setObjectName("pushButton_cari_edit")
        
        self.label_jenis_edit = QtWidgets.QLabel(self.groupBox_edit_pakaian)
        self.label_jenis_edit.setGeometry(QtCore.QRect(12, 110, 49, 21))
        self.label_jenis_edit.setObjectName("label_jenis_edit")
        
        self.cmb_jenis_edit = QtWidgets.QComboBox(self.groupBox_edit_pakaian)
        self.cmb_jenis_edit.setGeometry(QtCore.QRect(12, 146, 356, 31))
        self.cmb_jenis_edit.setObjectName("cmb_jenis_edit")
        
        self.label_nama_barang_edit = QtWidgets.QLabel(self.groupBox_edit_pakaian)
        self.label_nama_barang_edit.setGeometry(QtCore.QRect(12, 192, 118, 21))
        self.label_nama_barang_edit.setObjectName("label_nama_barang_edit")
        self.lineEdit_nama_barang_edit = QtWidgets.QLineEdit(self.groupBox_edit_pakaian)
        self.lineEdit_nama_barang_edit.setGeometry(QtCore.QRect(12, 228, 356, 31))
        self.lineEdit_nama_barang_edit.setObjectName("lineEdit_nama_barang_edit")
        
        self.label_ukuran_edit = QtWidgets.QLabel(self.groupBox_edit_pakaian)
        self.label_ukuran_edit.setGeometry(QtCore.QRect(12, 274, 65, 21))
        self.label_ukuran_edit.setObjectName("label_ukuran_edit")
        
        self.cmb_ukuran_edit = QtWidgets.QComboBox(self.groupBox_edit_pakaian)
        self.cmb_ukuran_edit.setGeometry(QtCore.QRect(12, 310, 356, 31))
        self.cmb_ukuran_edit.setObjectName("cmb_ukuran_edit")
        
        self.label_stok_edit = QtWidgets.QLabel(self.groupBox_edit_pakaian)
        self.label_stok_edit.setGeometry(QtCore.QRect(12, 356, 43, 21))
        self.label_stok_edit.setObjectName("label_stok_edit")
        self.lineEdit_stok_edit = QtWidgets.QLineEdit(self.groupBox_edit_pakaian)
        self.lineEdit_stok_edit.setGeometry(QtCore.QRect(12, 392, 356, 32))
        self.lineEdit_stok_edit.setObjectName("lineEdit_stok_edit")
        self.label_harga_edit = QtWidgets.QLabel(self.groupBox_edit_pakaian)
        self.label_harga_edit.setGeometry(QtCore.QRect(12, 438, 43, 21))
        self.label_harga_edit.setObjectName("label_harga_edit")
        self.lineEdit_harga_edit = QtWidgets.QLineEdit(self.groupBox_edit_pakaian)
        self.lineEdit_harga_edit.setGeometry(QtCore.QRect(12, 474, 351, 31))
        self.lineEdit_harga_edit.setObjectName("lineEdit_harga_edit")
        self.pushButton_update = QtWidgets.QPushButton(self.groupBox_edit_pakaian)
        self.pushButton_update.setGeometry(QtCore.QRect(60, 530, 121, 50))
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_cancel1 = QtWidgets.QPushButton(self.groupBox_edit_pakaian)
        self.pushButton_cancel1.setGeometry(QtCore.QRect(200, 530, 121, 50))
        self.pushButton_cancel1.setObjectName("pushButton_cancel1")
        
        self.tabWidget.addTab(self.tab_2, "Edit")
        
        # --- TAB HAPUS (DIUBAH KE LINEEDIT AGAR BISA PK003) ---
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_konfirmasi_hapus_pakaian = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_konfirmasi_hapus_pakaian.setGeometry(QtCore.QRect(15, 10, 380, 591))
        self.groupBox_konfirmasi_hapus_pakaian.setObjectName("groupBox_konfirmasi_hapus_pakaian")
        self.label_id_pakaian1 = QtWidgets.QLabel(self.groupBox_konfirmasi_hapus_pakaian)
        self.label_id_pakaian1.setGeometry(QtCore.QRect(12, 28, 97, 21))
        self.label_id_pakaian1.setObjectName("label_id_pakaian1")
        
        # PERUBAHAN: QSpinBox diganti menjadi QLineEdit
        self.lineEdit_id_pakaian_hapus = QtWidgets.QLineEdit(self.groupBox_konfirmasi_hapus_pakaian)
        self.lineEdit_id_pakaian_hapus.setGeometry(QtCore.QRect(12, 64, 298, 31))
        self.lineEdit_id_pakaian_hapus.setObjectName("lineEdit_id_pakaian_hapus")
        self.lineEdit_id_pakaian_hapus.setPlaceholderText("Masukkan ID (cth: PK003)")

        self.pushButton_cari_pakaian = QtWidgets.QPushButton(self.groupBox_konfirmasi_hapus_pakaian)
        self.pushButton_cari_pakaian.setGeometry(QtCore.QRect(322, 64, 46, 31))
        self.pushButton_cari_pakaian.setObjectName("pushButton_cari_pakaian")
        self.label_jenis1 = QtWidgets.QLabel(self.groupBox_konfirmasi_hapus_pakaian)
        self.label_jenis1.setGeometry(QtCore.QRect(12, 110, 49, 21))
        self.label_jenis1.setObjectName("label_jenis1")
        self.lineEdit_jenis1 = QtWidgets.QLineEdit(self.groupBox_konfirmasi_hapus_pakaian)
        self.lineEdit_jenis1.setGeometry(QtCore.QRect(12, 146, 356, 31))
        self.lineEdit_jenis1.setReadOnly(True)
        self.lineEdit_jenis1.setObjectName("lineEdit_jenis1")
        self.label_nama_barang1 = QtWidgets.QLabel(self.groupBox_konfirmasi_hapus_pakaian)
        self.label_nama_barang1.setGeometry(QtCore.QRect(12, 192, 118, 21))
        self.label_nama_barang1.setObjectName("label_nama_barang1")
        self.lineEdit_nama_barang1 = QtWidgets.QLineEdit(self.groupBox_konfirmasi_hapus_pakaian)
        self.lineEdit_nama_barang1.setGeometry(QtCore.QRect(12, 228, 356, 31))
        self.lineEdit_nama_barang1.setReadOnly(True)
        self.lineEdit_nama_barang1.setObjectName("lineEdit_nama_barang1")
        self.label_ukuran1 = QtWidgets.QLabel(self.groupBox_konfirmasi_hapus_pakaian)
        self.label_ukuran1.setGeometry(QtCore.QRect(12, 274, 65, 21))
        self.label_ukuran1.setObjectName("label_ukuran1")
        self.lineEdit_ukuran1 = QtWidgets.QLineEdit(self.groupBox_konfirmasi_hapus_pakaian)
        self.lineEdit_ukuran1.setGeometry(QtCore.QRect(12, 310, 356, 31))
        self.lineEdit_ukuran1.setReadOnly(True)
        self.lineEdit_ukuran1.setObjectName("lineEdit_ukuran1")
        self.label_stok1 = QtWidgets.QLabel(self.groupBox_konfirmasi_hapus_pakaian)
        self.label_stok1.setGeometry(QtCore.QRect(12, 356, 43, 21))
        self.label_stok1.setObjectName("label_stok1")
        self.lineEdit_stok1 = QtWidgets.QLineEdit(self.groupBox_konfirmasi_hapus_pakaian)
        self.lineEdit_stok1.setGeometry(QtCore.QRect(12, 392, 356, 32))
        self.lineEdit_stok1.setReadOnly(True)
        self.lineEdit_stok1.setObjectName("lineEdit_stok1")
        self.label_harga1 = QtWidgets.QLabel(self.groupBox_konfirmasi_hapus_pakaian)
        self.label_harga1.setGeometry(QtCore.QRect(12, 438, 51, 21))
        self.label_harga1.setObjectName("label_harga1")
        self.lineEdit_harga1 = QtWidgets.QLineEdit(self.groupBox_konfirmasi_hapus_pakaian)
        self.lineEdit_harga1.setGeometry(QtCore.QRect(12, 474, 351, 31))
        self.lineEdit_harga1.setReadOnly(True)
        self.lineEdit_harga1.setObjectName("lineEdit_harga1")
        self.pushButton_hapus = QtWidgets.QPushButton(self.groupBox_konfirmasi_hapus_pakaian)
        self.pushButton_hapus.setGeometry(QtCore.QRect(70, 530, 111, 50))
        self.pushButton_hapus.setObjectName("pushButton_hapus")
        self.pushButton_cancel2 = QtWidgets.QPushButton(self.groupBox_konfirmasi_hapus_pakaian)
        self.pushButton_cancel2.setGeometry(QtCore.QRect(200, 530, 121, 50))
        self.pushButton_cancel2.setObjectName("pushButton_cancel2")
        
        self.tabWidget.addTab(self.tab_3, "Hapus")

        self.retranslateUi(StokPakaianForm)
        self.tabWidget.setCurrentIndex(0)
        
        # --- LOGIKA & SINYAL ---
        self.populate_comboboxes()
        self.load_table_data()

        self.pushButton_simpan.clicked.connect(self.aksi_simpan)
        self.pushButton_cancel.clicked.connect(self.aksi_batal_tambah)

        self.pushButton_cari_edit.clicked.connect(self.aksi_cari_edit)
        self.pushButton_update.clicked.connect(self.aksi_update)
        self.pushButton_cancel1.clicked.connect(self.aksi_batal_edit)

        self.pushButton_cari_pakaian.clicked.connect(self.aksi_cari_hapus)
        self.pushButton_hapus.clicked.connect(self.aksi_hapus)
        self.pushButton_cancel2.clicked.connect(self.aksi_batal_hapus)

        self.backButton.clicked.connect(self.aksi_kembali)
        
        self.searchTermLineEdit.textChanged.connect(self.filter_search)
        self.filterKategoriComboBox.currentIndexChanged.connect(self.filter_search)

        QtCore.QMetaObject.connectSlotsByName(StokPakaianForm)

    def retranslateUi(self, StokPakaianForm):
        _translate = QtCore.QCoreApplication.translate
        StokPakaianForm.setWindowTitle(_translate("StokPakaianForm", "List Jenis Pakaian"))
        self.iconLabel.setText(_translate("StokPakaianForm", "📦"))
        self.titleLabel.setText(_translate("StokPakaianForm", "Kelola Jenis Pakaian"))
        self.searchIconLabel.setText(_translate("StokPakaianForm", "🔍"))
        self.searchTermLineEdit.setPlaceholderText(_translate("StokPakaianForm", "Cari ID, Jenis, atau Nama Pakaian..."))
        self.filterIconLabel.setText(_translate("StokPakaianForm", "⚙️"))
        self.filterKategoriComboBox.setItemText(0, _translate("StokPakaianForm", "Semua"))
        self.backButton.setText(_translate("StokPakaianForm", "Kembali"))
        self.groupBox_tambah_pakaian.setTitle(_translate("StokPakaianForm", "Detail Pakaian Baru"))
        self.label_id_pakaian.setText(_translate("StokPakaianForm", "ID Pakaian:"))
        self.lineEdit_id_pakaian.setPlaceholderText(_translate("StokPakaianForm", "Masukkan ID"))
        self.label_jenis.setText(_translate("StokPakaianForm", "Jenis:"))
        self.label_nama_barang.setText(_translate("StokPakaianForm", "Nama Barang:"))
        self.lineEdit_nama_barang.setPlaceholderText(_translate("StokPakaianForm", "Masukkan Nama"))
        self.label_ukuran.setText(_translate("StokPakaianForm", "Ukuran:"))
        self.label_stok.setText(_translate("StokPakaianForm", "Stok:"))
        self.lineEdit_stok.setPlaceholderText(_translate("StokPakaianForm", "Masukkan jumlah stok"))
        self.label_harga.setText(_translate("StokPakaianForm", "Harga:"))
        self.lineEdit_harga.setPlaceholderText(_translate("StokPakaianForm", "Masukkan harga"))
        self.pushButton_simpan.setText(_translate("StokPakaianForm", "Simpan"))
        self.pushButton_cancel.setText(_translate("StokPakaianForm", "Batal"))
        self.groupBox_edit_pakaian.setTitle(_translate("StokPakaianForm", "Detail Pakaian yang Akan Diperbarui"))
        self.label_id_pakaian_edit.setText(_translate("StokPakaianForm", "ID Pakaian:"))
        self.lineEdit_id_pakaian_edit.setPlaceholderText(_translate("StokPakaianForm", "Masukkan ID Pakaian"))
        self.pushButton_cari_edit.setText(_translate("StokPakaianForm", "Cari"))
        self.label_jenis_edit.setText(_translate("StokPakaianForm", "Jenis:"))
        self.label_nama_barang_edit.setText(_translate("StokPakaianForm", "Nama Barang:"))
        self.label_ukuran_edit.setText(_translate("StokPakaianForm", "Ukuran:"))
        self.label_stok_edit.setText(_translate("StokPakaianForm", "Stok:"))
        self.label_harga_edit.setText(_translate("StokPakaianForm", "Harga:"))
        self.pushButton_update.setText(_translate("StokPakaianForm", "Perbarui"))
        self.pushButton_cancel1.setText(_translate("StokPakaianForm", "Batal"))
        self.groupBox_konfirmasi_hapus_pakaian.setTitle(_translate("StokPakaianForm", "Detail Pakaian yang Akan Dihapus"))
        self.label_id_pakaian1.setText(_translate("StokPakaianForm", "ID Pakaian:"))
        self.pushButton_cari_pakaian.setText(_translate("StokPakaianForm", "Cari"))
        self.label_jenis1.setText(_translate("StokPakaianForm", "Jenis:"))
        self.label_nama_barang1.setText(_translate("StokPakaianForm", "Nama Barang:"))
        self.label_ukuran1.setText(_translate("StokPakaianForm", "Ukuran:"))
        self.label_stok1.setText(_translate("StokPakaianForm", "Stok:"))
        self.label_harga1.setText(_translate("StokPakaianForm", "Harga:"))
        self.pushButton_hapus.setText(_translate("StokPakaianForm", "Hapus"))
        self.pushButton_cancel2.setText(_translate("StokPakaianForm", "Batal"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("StokPakaianForm", "Tambah"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("StokPakaianForm", "Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("StokPakaianForm", "Hapus"))

    # =========================================================================
    # LOGIKA SISTEM (DATABASE & COMBOBOX)
    # =========================================================================

    def populate_comboboxes(self):
        try:
            list_jenis = Jenis.select_data()
            list_ukuran = Ukuran.select_data()

            self.cmb_jenis.clear()
            self.cmb_jenis.addItems(list_jenis)
            self.cmb_jenis_edit.clear()
            self.cmb_jenis_edit.addItems(list_jenis)
            
            self.filterKategoriComboBox.clear()
            self.filterKategoriComboBox.addItem("Semua")
            self.filterKategoriComboBox.addItems(list_jenis)

            self.cmb_ukuran.clear()
            self.cmb_ukuran.addItems(list_ukuran)
            self.cmb_ukuran_edit.clear()
            self.cmb_ukuran_edit.addItems(list_ukuran)
        except Exception as e:
            print(f"Error populate combo: {e}")

    def load_table_data(self):
        try:
            data = Barang.tampil_data() 
            self.stokTableWidget.setRowCount(len(data))
            kolom_center = [0, 3, 4, 5]
            for row_idx, row_data in enumerate(data):
                for col_idx, value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    if col_idx in kolom_center:
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.stokTableWidget.setItem(row_idx, col_idx, item)
        except Exception as e:
            print(f"Error loading table: {e}")

    def filter_search(self):
        search_text = self.searchTermLineEdit.text().lower()
        filter_jenis = self.filterKategoriComboBox.currentText().lower()

        for row in range(self.stokTableWidget.rowCount()):
            id_item = self.stokTableWidget.item(row, 0).text().lower()
            jenis_item = self.stokTableWidget.item(row, 1).text().lower()
            nama_item = self.stokTableWidget.item(row, 2).text().lower()

            match_search = (search_text in id_item) or (search_text in nama_item)
            match_filter = (filter_jenis == "semua") or (filter_jenis == jenis_item)

            self.stokTableWidget.setRowHidden(row, not (match_search and match_filter))

    # --- LOGIKA TAMBAH ---
    def aksi_simpan(self):
        id_pakaian = self.lineEdit_id_pakaian.text()
        jenis = self.cmb_jenis.currentText()
        nama = self.lineEdit_nama_barang.text()
        ukuran = self.cmb_ukuran.currentText()
        stok = self.lineEdit_stok.text()
        harga = self.lineEdit_harga.text()

        if id_pakaian == "" or nama == "" or stok == "" or harga == "":
            QMessageBox.warning(None, "Peringatan", "Data tidak boleh ada yang kosong!")
            return

        if Barang.cek_id_ada(id_pakaian):
            QMessageBox.warning(None, "Error", "ID sudah terpakai!")
            return

        try:
            Barang.insert_data(id_pakaian, jenis, nama, ukuran, stok, harga)
            QMessageBox.information(None, "Sukses", "Data berhasil ditambahkan!")
            self.load_table_data()
            self.aksi_batal_tambah()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal menyimpan: {e}")

    def aksi_batal_tambah(self):
        self.lineEdit_id_pakaian.clear()
        self.lineEdit_nama_barang.clear()
        self.lineEdit_stok.clear()
        self.lineEdit_harga.clear()
        self.cmb_jenis.setCurrentIndex(0)
        self.cmb_ukuran.setCurrentIndex(0)

    # --- LOGIKA EDIT ---
    def aksi_cari_edit(self):
        id_cari = self.lineEdit_id_pakaian_edit.text()
        if not id_cari:
            QMessageBox.warning(None, "Peringatan", "Masukkan ID Pakaian!")
            return

        data = Barang.select_data_by_id(id_cari)
        if data:
            self.cmb_jenis_edit.setCurrentText(str(data[1]))
            self.lineEdit_nama_barang_edit.setText(str(data[2]))
            self.cmb_ukuran_edit.setCurrentText(str(data[3]))
            self.lineEdit_stok_edit.setText(str(data[4]))
            self.lineEdit_harga_edit.setText(str(data[5]))
        else:
            QMessageBox.warning(None, "Error", "ID tidak ditemukan!")

    def aksi_update(self):
        id_pakaian = self.lineEdit_id_pakaian_edit.text()
        if not id_pakaian or self.lineEdit_nama_barang_edit.text() == "":
            QMessageBox.warning(None, "Peringatan", "Cari data terlebih dahulu!")
            return

        try:
            Barang.update_data(
                self.cmb_jenis_edit.currentText(),
                self.lineEdit_nama_barang_edit.text(),
                self.cmb_ukuran_edit.currentText(),
                self.lineEdit_stok_edit.text(),
                self.lineEdit_harga_edit.text(),
                id_pakaian
            )
            QMessageBox.information(None, "Sukses", "Data berhasil diperbarui!")
            self.load_table_data()
            self.aksi_batal_edit()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal update: {e}")

    def aksi_batal_edit(self):
        self.lineEdit_id_pakaian_edit.clear()
        self.lineEdit_nama_barang_edit.clear()
        self.lineEdit_stok_edit.clear()
        self.lineEdit_harga_edit.clear()
        self.cmb_jenis_edit.setCurrentIndex(0)
        self.cmb_ukuran_edit.setCurrentIndex(0)

    # --- LOGIKA HAPUS (FIXED: MENGGUNAKAN LINEEDIT UNTUK PK003) ---
    def aksi_cari_hapus(self):
        id_cari = self.lineEdit_id_pakaian_hapus.text() # Mengambil dari lineEdit, bukan spinbox
        if not id_cari:
            QMessageBox.warning(None, "Peringatan", "Masukkan ID Pakaian!")
            return

        try:
            data = Barang.select_data_by_id(id_cari)
            if data:
                self.lineEdit_jenis1.setText(str(data[1]))
                self.lineEdit_nama_barang1.setText(str(data[2]))
                self.lineEdit_ukuran1.setText(str(data[3]))
                self.lineEdit_stok1.setText(str(data[4]))
                self.lineEdit_harga1.setText(str(data[5]))
            else:
                QMessageBox.warning(None, "Info", "Data tidak ditemukan")
                self.aksi_batal_hapus()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal cari: {e}")

    def aksi_hapus(self):
        id_hapus = self.lineEdit_id_pakaian_hapus.text()
        if self.lineEdit_nama_barang1.text() == "":
            QMessageBox.warning(None, "Peringatan", "Cari data yang akan dihapus!")
            return

        confirm = QMessageBox.question(None, "Konfirmasi", "Yakin ingin menghapus data ini?", 
                                     QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                Barang.delete_data(id_hapus)
                QMessageBox.information(None, "Sukses", "Data berhasil dihapus")
                self.load_table_data()
                self.aksi_batal_hapus()
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Gagal menghapus: {e}")

    def aksi_batal_hapus(self):
        self.lineEdit_id_pakaian_hapus.clear() # Reset lineEdit hapus
        self.lineEdit_jenis1.clear()
        self.lineEdit_nama_barang1.clear()
        self.lineEdit_ukuran1.clear()
        self.lineEdit_stok1.clear()
        self.lineEdit_harga1.clear()

    def aksi_kembali(self):
        try:
            import form_dashboard_admin as back
            self.window_admin = QtWidgets.QMainWindow()
            self.ui_admin = back.Ui_MainWindow()
            self.ui_admin.setupUi(self.window_admin)
            self.window_admin.show()
            self.main_form.close()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal kembali: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    StokPakaianForm = QtWidgets.QWidget()
    ui = Ui_StokPakaianForm()
    ui.setupUi(StokPakaianForm)
    StokPakaianForm.show()
    sys.exit(app.exec_())