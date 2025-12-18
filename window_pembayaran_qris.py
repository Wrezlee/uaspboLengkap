# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class WindowProsesPembayaran(QtWidgets.QDialog):
    def __init__(self, total_bayar, parent=None):
        super().__init__(parent)
        self.total_bayar = total_bayar
        self.bayar = 0
        self.kembalian = 0
        self.setWindowTitle("Proses Pembayaran - KELOMPOK 1")
        self.setFixedSize(460, 520)
        self.setStyleSheet("background-color: #E3F2FD;")

        layout = QtWidgets.QVBoxLayout(self)

        # ===== JUDUL =====
        judul = QtWidgets.QLabel("PROSES PEMBAYARAN")
        judul.setAlignment(QtCore.Qt.AlignCenter)
        judul.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))

        merchant = QtWidgets.QLabel("Merchant : KELOMPOK 1")
        merchant.setAlignment(QtCore.Qt.AlignCenter)
        merchant.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))

        # ===== TOTAL =====
        self.label_total = QtWidgets.QLabel(
            f"TOTAL : Rp {total_bayar:,}".replace(",", ".")
        )
        self.label_total.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.label_total.setStyleSheet("color: red;")

        # ===== METODE =====
        metode_label = QtWidgets.QLabel("Metode Pembayaran")
        self.combo_metode = QtWidgets.QComboBox()
        self.combo_metode.addItems(["Cash", "QRIS", "Debit"])

        # ===== QRIS IMAGE =====
        self.label_qr = QtWidgets.QLabel()
        self.label_qr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qr.setVisible(False)

        pixmap = QtGui.QPixmap("qris_kelompok1.png")
        pixmap = pixmap.scaled(220, 220, QtCore.Qt.KeepAspectRatio)
        self.label_qr.setPixmap(pixmap)

        # ===== UANG =====
        uang_label = QtWidgets.QLabel("Uang Pelanggan")
        self.input_uang = QtWidgets.QLineEdit()
        self.input_uang.setPlaceholderText("Masukkan uang pelanggan")

        # ===== KEMBALIAN =====
        self.label_kembalian = QtWidgets.QLabel("Kembalian : Rp 0")
        self.label_kembalian.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kembalian.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        # ===== BUTTON =====
        btn_layout = QtWidgets.QHBoxLayout()
        btn_selesai = QtWidgets.QPushButton("SELESAI")
        btn_batal = QtWidgets.QPushButton("BATAL")

        btn_layout.addWidget(btn_batal)
        btn_layout.addWidget(btn_selesai)

        # ===== LAYOUT =====
        layout.addWidget(judul)
        layout.addWidget(merchant)
        layout.addSpacing(10)
        layout.addWidget(self.label_total)
        layout.addSpacing(10)
        layout.addWidget(metode_label)
        layout.addWidget(self.combo_metode)
        layout.addWidget(self.label_qr)
        layout.addWidget(uang_label)
        layout.addWidget(self.input_uang)
        layout.addWidget(self.label_kembalian)
        layout.addStretch()
        layout.addLayout(btn_layout)

        # ===== EVENT =====
        self.combo_metode.currentTextChanged.connect(self.toggle_metode)
        self.input_uang.textChanged.connect(self.hitung_kembalian)
        btn_selesai.clicked.connect(self.validasi)
        btn_batal.clicked.connect(self.reject)

    def toggle_metode(self, metode):
        if metode == "QRIS":
            self.label_qr.setVisible(True)
            self.input_uang.setDisabled(True)
            self.label_kembalian.setText("Silakan scan QRIS")
        else:
            self.label_qr.setVisible(False)
            self.input_uang.setDisabled(False)
            self.label_kembalian.setText("Kembalian : Rp 0")

    def hitung_kembalian(self):
        try:
            uang = int(self.input_uang.text())

            kembalian = uang - self.total_bayar
            if kembalian < 0:
                self.label_kembalian.setText("Uang kurang")
            else:
                self.label_kembalian.setText(
                    f"Kembalian : Rp {kembalian:,}".replace(",", ".")
                )
        except:
            self.label_kembalian.setText("Kembalian : Rp 0")

    def validasi(self):
        metode = self.combo_metode.currentText()

        # ===== QRIS =====
        if metode == "QRIS":
            self.bayar = self.total_bayar
            self.kembalian = 0
            QMessageBox.information(self, "QRIS", "Pembayaran QRIS berhasil")
            self.accept()
            return

        # ===== CASH / DEBIT =====
        try:
            uang = int(self.input_uang.text())
        except:
            QMessageBox.warning(self, "Error", "Masukkan uang yang valid")
            return

        if uang < self.total_bayar:
            QMessageBox.warning(self, "Uang Kurang", "Uang pelanggan tidak cukup")
            return

        self.bayar = uang
        self.kembalian = uang - self.total_bayar
        self.accept()


    def get_metode(self):
        return self.combo_metode.currentText()
    
    def get_bayar(self):
        return self.bayar

    def get_kembalian(self):
        return self.kembalian



# =====================================================
# ================== MAIN PROGRAM =====================
# =====================================================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    QMessageBox.information(
        None,
        "Info",
        "Window ini tidak dijalankan mandiri.\n"
        "Panggil dari halaman penjualan dengan mengirim total bayar."
    )

    sys.exit(0)
