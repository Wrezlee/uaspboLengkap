# -*- coding: utf-8 -*-
import sys
import mysql.connector
from PyQt5 import QtWidgets, QtCore, QtGui

# Gunakan alias 'as' agar nama class yang sama tidak saling menimpa
from dashboard_kasir import Ui_MainWindow as Ui_Kasir
from form_dashboard_admin import Ui_MainWindow as Ui_Admin

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Sistem")
        self.resize(800, 500)
        self.setStyleSheet("background-color: #e3f2fd;")

        self.card = QtWidgets.QFrame(self)
        self.card.setGeometry(200, 70, 400, 360)
        self.card.setStyleSheet("""
            QFrame {
                background-color: #bbdefb;
                border-radius: 25px;
                border: 2px solid #90caf9;
            }
        """)

        self.title = QtWidgets.QLabel("Silakan Login", self.card)
        self.title.setGeometry(0, 30, 400, 40)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            color: #0d47a1;
        """)

        self.username = QtWidgets.QLineEdit(self.card)
        self.username.setGeometry(80, 110, 240, 45)
        self.username.setPlaceholderText("Username")
        self.username.setStyleSheet("""
            QLineEdit {
                background-color: #90caf9;
                padding: 12px;
                border-radius: 12px;
                border: none;
                font-size: 16px;
                color: #0d47a1;
            }
        """)

        self.password = QtWidgets.QLineEdit(self.card)
        self.password.setGeometry(80, 170, 240, 45)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet("""
            QLineEdit {
                background-color: #90caf9;
                padding: 12px;
                border-radius: 12px;
                border: none;
                font-size: 16px;
                color: #0d47a1;
            }
        """)

        self.login_btn = QtWidgets.QPushButton("Login", self.card)
        self.login_btn.setGeometry(130, 240, 140, 50)
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #64b5f6;
                color: white;
                font-size: 18px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #42a5f5;
            }
        """)
        self.login_btn.clicked.connect(self.check_login)

    def check_login(self):
        username = self.username.text()
        password = self.password.text()

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pbo_uas"
            )
            cursor = db.cursor()

            sql = """
                SELECT username, password, nama_lengkap, level
                FROM users
                WHERE username=%s AND password=%s
            """
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            if user:
                nama = user[2]
                level = user[3] # Mengambil level dari database

                self.open_main(nama, level)
            else:
                QtWidgets.QMessageBox.warning(self, "Gagal", "Username atau password salah.")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def open_main(self, nama, level):
        # Kirim data nama dan level ke class MainWindow
        self.main = MainWindow(nama, level)
        self.main.show()
        self.close()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, nama, level):
        super().__init__()

        # Logika Percabangan untuk menentukan UI berdasarkan Level
        if level.lower() == "admin":
            self.ui = Ui_Admin()
            self.ui.setupUi(self)
            # Opsional: Jika di dashboard admin ada label untuk nama admin
            if hasattr(self.ui, 'titleLabel_2'):
                self.ui.titleLabel_2.setText(f"Halo Admin, {nama}!")
        else:
            # Default ke Kasir jika bukan Admin
            self.ui = Ui_Kasir()
            self.ui.setupUi(self)
            # Set nama pada label_2 milik kasir
            if hasattr(self.ui, 'label_2'):
                self.ui.label_2.setText(f"Halo, {nama}!")


# ===============================================================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = LoginWindow()
    win.show()
    sys.exit(app.exec_())