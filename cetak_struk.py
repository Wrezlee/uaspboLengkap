# cetak_struk.py
from PyQt5 import QtWidgets, uic
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import mysql.connector
import sys


# ================= DATABASE =================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pbo_uas"
    )


# ================= WINDOW =================
class CetakStrukWindow(QtWidgets.QMainWindow):
    def __init__(self, id_penjualan):
        super().__init__()

        uic.loadUi("cetak_struk.ui", self)

        self.id_penjualan = id_penjualan

        self.load_data()

        self.pushButton_print.clicked.connect(self.print_struk)
        self.pushButton_kembali.clicked.connect(self.close)
        self.pushButton_back.clicked.connect(self.close)

    # ================= LOAD DATA =================
    def load_data(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # ===== HEADER PENJUALAN =====
        cursor.execute("""
            SELECT no_faktur, tanggal, role,
                   subtotal, diskon, pajak, total
            FROM penjualan
            WHERE no_faktur = %s
        """, (self.id_penjualan,))
        header = cursor.fetchone()

        if not header:
            QtWidgets.QMessageBox.warning(self, "Error", "Data tidak ditemukan")
            return

        self.label_no_struk.setText(f"No: {header['no_faktur']}")
        self.label_tanggal.setText(f"Tanggal: {header['tanggal']}")
        self.label_kasir.setText(f"Role: {header['role']}")

        # ===== DETAIL PENJUALAN =====
        cursor.execute("""
            SELECT nama_barang, ukuran, warna, qty, harga, subtotal
            FROM detail_penjualan
            WHERE id_penjualan = %s
        """, (self.id_penjualan,))
        detail = cursor.fetchall()

        text = ""

        for d in detail:
            text += f"{d['nama_barang']} ({d['ukuran']} / {d['warna']})\n"
            text += f"{d['qty']} x Rp {int(d['harga']):,} = Rp {int(d['subtotal']):,}\n\n"

        self.textEdit_detail.setText(text)

        # ===== TOTAL =====
        self.label_subtotal.setText(
            f"Sub Total:      Rp {int(header['subtotal']):,}"
        )
        self.label_diskon.setText(
            f"Diskon ({header['diskon']}%):  Rp {(header['subtotal'] * header['diskon']) // 100:,}"
        )
        self.label_pajak.setText(
            f"Pajak ({header['pajak']}%):   Rp {(header['subtotal'] * header['pajak']) // 100:,}"
        )
        self.label_total.setText(
            f"TOTAL:         Rp {int(header['total']):,}"
        )

        cursor.close()
        conn.close()

    # ================= PRINT =================
    def print_struk(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.groupBox_struk.render(printer)


# ================= TEST =================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CetakStrukWindow(1)  # ganti ID sesuai transaksi
    window.show()
    sys.exit(app.exec_())
