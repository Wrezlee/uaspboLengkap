# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hapususer.ui'
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_FormHapusUser(object):
    def setupUi(self, FormHapusUser):
        self.mainwindow_ref = FormHapusUser # Referensi untuk menutup window
        FormHapusUser.setObjectName("FormHapusUser")
        FormHapusUser.resize(687, 795)
        FormHapusUser.setStyleSheet("\n"
"    QWidget { background-color: #121212; color: #E0E0E0; font-family: 'Segoe UI', sans-serif; font-size: 11pt; }\n"
"    QGroupBox { background-color: #1E1E1E; border: 1px solid #333333; border-radius: 12px; margin-top: 24px; font-weight: bold; }\n"
"    QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #FF5252; }\n"
"    QLabel { color: #B0B0B0; }\n"
"    QLineEdit { background-color: #2D2D2D; border: 1px solid #404040; border-radius: 8px; padding: 8px; color: #9E9E9E; }\n"
"    QLineEdit:enabled { color: white; }\n"
"    QPushButton { background-color: #333333; border: 1px solid #444444; border-radius: 8px; padding: 10px; color: white; font-weight: bold; }\n"
"    QPushButton#pushButton_cari { background-color: #2962FF; border: none; }\n"
"    QPushButton#pushButton_hapus, QPushButton#pushButton_cancel { background-color: #D32F2F; border: none; }\n"
"    QPushButton#pushButton_hapus:hover { background-color: #B71C1C; }\n"
"    QPushButton#pushButton_kembali { background-color: #2962FF; }\n"
"   ")
        self.mainLayout = QtWidgets.QVBoxLayout(FormHapusUser)
        self.mainLayout.setObjectName("mainLayout")
        self.label_title = QtWidgets.QLabel(FormHapusUser)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.mainLayout.addWidget(self.label_title)
        self.groupBox_hapus_user = QtWidgets.QGroupBox(FormHapusUser)
        self.groupBox_hapus_user.setObjectName("groupBox_hapus_user")
        self.formLayout = QtWidgets.QVBoxLayout(self.groupBox_hapus_user)
        self.formLayout.setObjectName("formLayout")
        self.label_id = QtWidgets.QLabel(self.groupBox_hapus_user)
        self.label_id.setObjectName("label_id")
        self.formLayout.addWidget(self.label_id)
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLayout.setObjectName("searchLayout")
        self.lineEdit_id = QtWidgets.QLineEdit(self.groupBox_hapus_user)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.searchLayout.addWidget(self.lineEdit_id)
        self.pushButton_cari = QtWidgets.QPushButton(self.groupBox_hapus_user)
        self.pushButton_cari.setObjectName("pushButton_cari")
        self.searchLayout.addWidget(self.pushButton_cari)
        self.formLayout.addLayout(self.searchLayout)
        self.label_nama = QtWidgets.QLabel(self.groupBox_hapus_user)
        self.label_nama.setObjectName("label_nama")
        self.formLayout.addWidget(self.label_nama)
        self.lineEdit_nama = QtWidgets.QLineEdit(self.groupBox_hapus_user)
        self.lineEdit_nama.setReadOnly(True)
        self.lineEdit_nama.setObjectName("lineEdit_nama")
        self.formLayout.addWidget(self.lineEdit_nama)
        self.label_username = QtWidgets.QLabel(self.groupBox_hapus_user)
        self.label_username.setObjectName("label_username")
        self.formLayout.addWidget(self.label_username)
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox_hapus_user)
        self.lineEdit_username.setReadOnly(True)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.formLayout.addWidget(self.lineEdit_username)
        self.label_level = QtWidgets.QLabel(self.groupBox_hapus_user)
        self.label_level.setObjectName("label_level")
        self.formLayout.addWidget(self.label_level)
        self.lineEdit_level = QtWidgets.QLineEdit(self.groupBox_hapus_user)
        self.lineEdit_level.setReadOnly(True)
        self.lineEdit_level.setObjectName("lineEdit_level")
        self.formLayout.addWidget(self.lineEdit_level)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.addItem(spacerItem)
        self.pushButton_hapus = QtWidgets.QPushButton(self.groupBox_hapus_user)
        self.pushButton_hapus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_hapus.setObjectName("pushButton_hapus")
        self.formLayout.addWidget(self.pushButton_hapus)
        self.mainLayout.addWidget(self.groupBox_hapus_user)
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.setObjectName("bottomLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem1)
        self.pushButton_kembali = QtWidgets.QPushButton(FormHapusUser)
        self.pushButton_kembali.setObjectName("pushButton_kembali")
        self.bottomLayout.addWidget(self.pushButton_kembali)
        self.mainLayout.addLayout(self.bottomLayout)

        self.retranslateUi(FormHapusUser)
        QtCore.QMetaObject.connectSlotsByName(FormHapusUser)

        # --- HUBUNGKAN LOGIKA TOMBOL ---
        self.pushButton_cari.clicked.connect(self.aksi_cari)
        self.pushButton_hapus.clicked.connect(self.aksi_hapus)
        self.pushButton_kembali.clicked.connect(self.aksi_kembali)

    def retranslateUi(self, FormHapusUser):
        _translate = QtCore.QCoreApplication.translate
        FormHapusUser.setWindowTitle(_translate("FormHapusUser", "Hapus User"))
        self.label_title.setStyleSheet(_translate("FormHapusUser", "font-size: 36px; font-weight: bold; color: white; margin-bottom: 20px;"))
        self.label_title.setText(_translate("FormHapusUser", "Hapus User"))
        self.groupBox_hapus_user.setTitle(_translate("FormHapusUser", "Konfirmasi Hapus"))
        self.label_id.setText(_translate("FormHapusUser", "Cari Username User:"))
        self.lineEdit_id.setPlaceholderText(_translate("FormHapusUser", "Masukkan Username..."))
        self.pushButton_cari.setText(_translate("FormHapusUser", "🔍 Cari"))
        self.label_nama.setText(_translate("FormHapusUser", "Nama:"))
        self.label_username.setText(_translate("FormHapusUser", "Username:"))
        self.label_level.setText(_translate("FormHapusUser", "Level:"))
        self.pushButton_hapus.setText(_translate("FormHapusUser", "🗑 Hapus Permanen"))
        self.pushButton_kembali.setText(_translate("FormHapusUser", "Kembali"))

    # ================= LOGIKA DATABASE =================
    def aksi_cari(self):
        username_cari = self.lineEdit_id.text().strip()
        if not username_cari:
            QMessageBox.warning(None, "Peringatan", "Masukkan username yang ingin dicari!")
            return

        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pbo_uas")
            cursor = mydb.cursor()
            query = "SELECT nama_lengkap, username, level FROM users WHERE username = %s OR nama_lengkap = %s"
            cursor.execute(query, (username_cari, username_cari))
            result = cursor.fetchone()

            if result:
                self.lineEdit_nama.setText(result[0])
                self.lineEdit_username.setText(result[1])
                self.lineEdit_level.setText(result[2])
                QMessageBox.information(None, "Sukses", "Data ditemukan! Silakan konfirmasi penghapusan.")
            else:
                QMessageBox.warning(None, "Gagal", "Data tidak ditemukan.")
                self.lineEdit_nama.clear()
                self.lineEdit_username.clear()
                self.lineEdit_level.clear()
            
            mydb.close()
        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Error Database", f"Terjadi kesalahan: {err}")

    def aksi_hapus(self):
        username_target = self.lineEdit_username.text()
        
        if not username_target:
            QMessageBox.warning(None, "Peringatan", "Cari data user yang akan dihapus terlebih dahulu!")
            return

        confirm = QMessageBox.question(None, "Konfirmasi Hapus", 
                                     f"Apakah Anda yakin ingin menghapus user '{username_target}' secara permanen?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if confirm == QMessageBox.Yes:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pbo_uas")
                cursor = mydb.cursor()
                
                sql = "DELETE FROM users WHERE username = %s"
                cursor.execute(sql, (username_target,))
                mydb.commit()

                if cursor.rowcount > 0:
                    QMessageBox.information(None, "Sukses", "Data User berhasil dihapus!")
                    # self.aksi_kembali() <--- BARIS INI DIHAPUS AGAR TIDAK LANGSUNG KEMBALI
                    
                    # Opsional: Bersihkan field agar form kosong setelah hapus
                    self.lineEdit_nama.clear()
                    self.lineEdit_username.clear()
                    self.lineEdit_level.clear()
                    self.lineEdit_id.clear()
                else:
                    QMessageBox.warning(None, "Gagal", "Data gagal dihapus atau sudah tidak ada.")
                
                mydb.close()
            except mysql.connector.Error as err:
                QMessageBox.critical(None, "Error Database", f"Gagal menghapus: {err}")

    # ================= LOGIKA NAVIGASI KEMBALI =================
    def aksi_kembali(self):
        try:
            from form_list_user import Ui_FormListUser
            self.window_list = QtWidgets.QMainWindow()
            self.ui_list = Ui_FormListUser()
            self.ui_list.setupUi(self.window_list)
            self.window_list.show()
            self.mainwindow_ref.close() 
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Gagal memuat halaman List User:\n{e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormHapusUser = QtWidgets.QWidget()
    ui = Ui_FormHapusUser()
    ui.setupUi(FormHapusUser)
    FormHapusUser.show()
    sys.exit(app.exec_())