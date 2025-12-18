# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import mysql.connector


# ================= DATABASE =================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbo_uas"
    )


# ================= WINDOW DETAIL =================
class DetailPenjualanWindow(QtWidgets.QMainWindow):
    def __init__(self, id_penjualan):
        super().__init__()
        self.id_penjualan = id_penjualan
        self.setWindowTitle(f"Detail Penjualan - ID: {id_penjualan}")
        self.resize(900, 700)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setStyleSheet(
            "QWidget { background-color: #E3F2FD; }"
        )

        # ===== MAIN LAYOUT =====
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 20, 30, 30)

        # ===== TITLE =====
        self.label = QtWidgets.QLabel(
            "DETAIL TRANSAKSI PENJUALAN 🧾"
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet(
            "color: #0D47A1; font: bold 24pt 'Times New Roman';"
        )
        main_layout.addWidget(self.label)

        # ===== INFO TRANSAKSI =====
        info_group = QtWidgets.QGroupBox("Informasi Transaksi")
        info_group.setStyleSheet("""
            QGroupBox {
                background-color: white;
                border: 2px solid #2196F3;
                border-radius: 10px;
                font: bold 14pt "Times New Roman";
                color: #0D47A1;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 20px;
                padding: 0 10px 0 10px;
            }
        """)
        
        info_layout = QtWidgets.QGridLayout()
        info_layout.setSpacing(15)
        
        # Info Header Transaksi
        labels_info = ["No. Faktur:", "Tanggal:", "Role:", "Total:", "Bayar:", "Kembalian:", "Diskon:", "Pajak:", "Subtotal:"]
        self.fields_info = []
        
        for i, label_text in enumerate(labels_info):
            # Label
            label = QtWidgets.QLabel(label_text)
            label.setStyleSheet("font: 12pt 'Times New Roman'; color: #333333;")
            info_layout.addWidget(label, i//3, (i%3)*2)
            
            # Field
            field = QtWidgets.QLineEdit()
            field.setReadOnly(True)
            field.setMinimumHeight(35)
            field.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #BBDEFB;
                    border-radius: 5px;
                    background-color: #F5F5F5;
                    font: 11pt 'Times New Roman';
                    padding: 5px;
                }
            """)
            info_layout.addWidget(field, i//3, (i%3)*2 + 1)
            self.fields_info.append(field)
        
        info_group.setLayout(info_layout)
        main_layout.addWidget(info_group)

        # ===== DETAIL BARANG =====
        detail_group = QtWidgets.QGroupBox("Detail Barang")
        detail_group.setStyleSheet("""
            QGroupBox {
                background-color: white;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                font: bold 14pt "Times New Roman";
                color: #2E7D32;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 20px;
                padding: 0 10px 0 10px;
            }
        """)

        detail_layout = QtWidgets.QGridLayout()
        detail_layout.setSpacing(15)

        self.table_detail = QtWidgets.QTableWidget()
        self.table_detail.setColumnCount(6)
        self.table_detail.setHorizontalHeaderLabels([
            "Nama Barang", "Ukuran", "Warna", "Qty", "Harga", "Subtotal"
        ])
        self.table_detail.horizontalHeader().setStretchLastSection(True)
        self.table_detail.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        detail_layout.addWidget(self.table_detail, 0, 0)

        detail_group.setLayout(detail_layout)

        main_layout.addWidget(detail_group)

        
        # Detail Barang
        
        
        detail_group.setLayout(detail_layout)
        main_layout.addWidget(detail_group)

        # ===== TOMBOL ACTION =====
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(20)
        
        # Tombol Cetak Struk
        self.btn_cetak = QtWidgets.QPushButton("🖨️ CETAK STRUK")
        self.btn_cetak.setMinimumHeight(50)
        self.btn_cetak.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                font: bold 14pt "Times New Roman";
            }
            QPushButton:hover {
                background-color: #388E3C;
                border: 2px solid #2E7D32;
            }
            QPushButton:pressed {
                background-color: #2E7D32;
            }
        """)
        self.btn_cetak.clicked.connect(self.cetak_struk)
        button_layout.addWidget(self.btn_cetak)
        
        # Tombol Tutup
        self.btn_tutup = QtWidgets.QPushButton("❌ TUTUP")
        self.btn_tutup.setMinimumHeight(50)
        self.btn_tutup.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                border-radius: 8px;
                font: bold 14pt "Times New Roman";
            }
            QPushButton:hover {
                background-color: #D32F2F;
                border: 2px solid #C62828;
            }
            QPushButton:pressed {
                background-color: #B71C1C;
            }
        """)
        self.btn_tutup.clicked.connect(self.close)
        button_layout.addWidget(self.btn_tutup)
        
        main_layout.addLayout(button_layout)
        
        # ===== STATUS BAR =====
        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage(f"Memuat detail transaksi ID: {id_penjualan}...")

        # ===== LOAD DATA =====
        self.load_data()

    # ================= LOAD DATA =================
    def load_data(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Query untuk mengambil data dari penjualan
            query_penjualan = """
                    SELECT 
                        no_faktur,
                        DATE_FORMAT(tanggal, '%d-%m-%Y') as tanggal,
                        role,
                        total,
                        bayar,
                        kembalian,
                        diskon,
                        pajak,
                        subtotal
                    FROM penjualan 
                    WHERE no_faktur = %s
                    """   
            cursor.execute(query_penjualan, (self.id_penjualan,))
            data_penjualan = cursor.fetchone()
            
            if not data_penjualan:
                self.status_bar.showMessage("Data transaksi tidak ditemukan!")
                QtWidgets.QMessageBox.warning(
                    self, "Error", f"Transaksi dengan ID {self.id_penjualan} tidak ditemukan!"
                )
                return
            
            # Isi data informasi transaksi
            for i, value in enumerate(data_penjualan):
                if i < len(self.fields_info):
                    if value is None:
                        text = "-"
                    elif isinstance(value, float):
                        if i in [3, 4, 5, 8]:  # total, bazar, kembalian, subtotal
                            text = f"Rp {value:,.2f}"
                        elif i in [6, 7]:  # diskon, pajak
                            text = f"{value}%"
                        else:
                            text = str(value)
                    else:
                        text = str(value)
                    self.fields_info[i].setText(text)
            
            # Query untuk mengambil data detail_penjualan
            query_detail = """
                    SELECT 
                        nama_barang,
                        ukuran,
                        warna,
                        qty,
                        harga,
                        subtotal
                    FROM detail_penjualan 
                    WHERE id_penjualan = %s
                    """

            
            cursor.execute(query_detail, (self.id_penjualan,))
            data_detail = cursor.fetchall()

            if not data_detail:
                self.table_detail.setRowCount(0)
                self.status_bar.showMessage("Detail barang tidak ditemukan!")
            else:
                self.table_detail.setRowCount(len(data_detail))
                for row, d in enumerate(data_detail):
                    for col, value in enumerate(d):
                        item = QtWidgets.QTableWidgetItem(str(value))
                        self.table_detail.setItem(row, col, item)

                self.status_bar.showMessage("Detail barang tidak ditemukan!")
            
            conn.close()
            
            # Update status bar
            self.status_bar.showMessage(f"Transaksi {data_penjualan[0]} - {data_penjualan[1]}")

        except mysql.connector.Error as e:
            self.status_bar.showMessage(f"Database error: {str(e)}")
            QtWidgets.QMessageBox.critical(
                self, "Database Error", 
                f"Terjadi kesalahan saat mengambil data:\n{str(e)}"
            )
        except Exception as e:
            self.status_bar.showMessage(f"Error: {str(e)}")
            QtWidgets.QMessageBox.critical(
                self, "Error", 
                f"Terjadi kesalahan:\n{str(e)}"
            )

    # ================= CETAK STRUK =================
    def cetak_struk(self):
        try:
            no_faktur = self.fields_info[0].text()
            tanggal = self.fields_info[1].text()
            total = self.fields_info[3].text()
            kembalian = self.fields_info[5].text()

            struk_text = f"""
        {'='*40}
        {'TOKO SERBA ADA'.center(40)}
        {'='*40}
        No. Faktur   : {no_faktur}
        Tanggal      : {tanggal}
        {'='*40}
        DETAIL BARANG:
        {'='*40}
        """

            for row in range(self.table_detail.rowCount()):
                nama = self.table_detail.item(row, 0).text()
                qty = self.table_detail.item(row, 3).text()
                harga = self.table_detail.item(row, 4).text()
                subtotal = self.table_detail.item(row, 5).text()

                struk_text += f"""
        {nama}
        {qty} x {harga} = {subtotal}
        {'-'*40}
        """

            struk_text += f"""
        {'='*40}
        Total        : {total}
        Kembalian    : {kembalian}
        {'='*40}
        {'TERIMA KASIH'.center(40)}
        {'='*40}
        """
    
            # Tampilkan preview struk
            preview_dialog = QtWidgets.QDialog(self)
            preview_dialog.setWindowTitle("Preview Struk")
            preview_dialog.resize(400, 500)
            
            layout = QtWidgets.QVBoxLayout()
            
            # Text edit untuk preview
            text_edit = QtWidgets.QTextEdit()
            text_edit.setPlainText(struk_text)
            text_edit.setReadOnly(True)
            text_edit.setFont(QtGui.QFont("Courier New", 10))
            layout.addWidget(text_edit)
            
            # Tombol untuk cetak
            btn_print = QtWidgets.QPushButton("🖨️ Cetak Struk")
            btn_print.clicked.connect(lambda: self.real_cetak_struk(struk_text))
            layout.addWidget(btn_print)
            
            btn_close = QtWidgets.QPushButton("Tutup")
            btn_close.clicked.connect(preview_dialog.close)
            layout.addWidget(btn_close)
            
            preview_dialog.setLayout(layout)
            preview_dialog.exec_()
            
        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self, "Error", 
                f"Gagal membuat struk:\n{str(e)}"
            )
    
    def real_cetak_struk(self, struk_text):
        """Simulasi cetak struk (bisa diganti dengan printer sebenarnya)"""
        try:
            # Simpan ke file
            filename = f"struk_{self.fields_info[0].text()}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(struk_text)
            
            # Tampilkan konfirmasi
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Struk Berhasil Dicetak")
            msg.setText(f"Struk telah disimpan sebagai:\n{filename}")
            msg.setDetailedText(struk_text)
            msg.exec_()
            
            self.status_bar.showMessage(f"Struk disimpan sebagai {filename}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self, "Error", 
                f"Gagal menyimpan struk:\n{str(e)}"
            )


# ================= WINDOW INPUT ID =================
class InputIdWindow(QtWidgets.QDialog):
    """Window untuk input ID penjualan sebelum membuka detail"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cari Detail Penjualan")
        self.resize(400, 200)
        
        self.setStyleSheet("""
            QWidget { background-color: #E3F2FD; }
        """)
        
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Label
        label = QtWidgets.QLabel("Masukkan ID Penjualan:")
        label.setStyleSheet("font: bold 14pt 'Times New Roman'; color: #0D47A1;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)
        
        # Input ID
        self.input_id = QtWidgets.QSpinBox()
        self.input_id.setRange(1, 999999)
        self.input_id.setMinimumHeight(40)
        self.input_id.setStyleSheet("""
            QSpinBox {
                font: 14pt 'Times New Roman';
                border: 2px solid #2196F3;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        layout.addWidget(self.input_id)
        
        # Tombol
        button_layout = QtWidgets.QHBoxLayout()
        
        btn_cari = QtWidgets.QPushButton("🔍 TAMPILKAN DETAIL")
        btn_cari.setMinimumHeight(45)
        btn_cari.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                font: bold 12pt "Times New Roman";
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
        """)
        btn_cari.clicked.connect(self.accept)
        button_layout.addWidget(btn_cari)
        
        btn_batal = QtWidgets.QPushButton("BATAL")
        btn_batal.setMinimumHeight(45)
        btn_batal.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
                color: white;
                border-radius: 8px;
                font: bold 12pt "Times New Roman";
            }
            QPushButton:hover {
                background-color: #D32F2F;
            }
        """)
        btn_batal.clicked.connect(self.reject)
        button_layout.addWidget(btn_batal)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def get_id_penjualan(self):
        return self.input_id.value()


# ================= RUN =================
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Pertama, tampilkan window untuk input ID
    input_window = InputIdWindow()
    if input_window.exec_() == QtWidgets.QDialog.Accepted:
        id_penjualan = input_window.get_id_penjualan()
        
        # Kemudian tampilkan detail penjualan
        window = DetailPenjualanWindow(id_penjualan)
        window.show()
        
        sys.exit(app.exec_())
    else:
        sys.exit(0)