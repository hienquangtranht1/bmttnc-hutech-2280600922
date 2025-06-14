from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit,
    QPushButton, QLabel, QComboBox
)
import sys
import hashlib
from Crypto.Hash import SHA3_256

def calculate_md5_library(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5_custom(message):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476

    original_length = len(message)
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]
        a0, b0, c0, d0 = h0, h1, h2, h3
        for j in range(64):
            if 0 <= j <= 15:
                f = (b0 & c0) | (~b0 & d0)
                g = j
                s = [7, 12, 17, 22] * 4
            elif 16 <= j <= 31:
                f = (d0 & b0) | (~d0 & c0)
                g = (j * 5 + 1) % 16
                s = [5, 9, 14, 20] * 4
            elif 32 <= j <= 47:
                f = b0 ^ c0 ^ d0
                g = (j * 3 + 5) % 16
                s = [4, 11, 16, 23] * 4
            elif 48 <= j <= 63:
                f = c0 ^ (b0 | ~d0)
                g = (j * 7) % 16
                s = [6, 10, 15, 21] * 4
            temp = d0
            d0 = c0
            c0 = b0
            b0 = (b0 + left_rotate(a0 + f + 0x5A827999 + words[g], s[j % 4])) & 0xFFFFFFFF
            a0 = temp
        h0 = (h0 + a0) & 0xFFFFFFFF
        h1 = (h1 + b0) & 0xFFFFFFFF
        h2 = (h2 + c0) & 0xFFFFFFFF
        h3 = (h3 + d0) & 0xFFFFFFFF
    return (h0.to_bytes(4, 'little') + h1.to_bytes(4, 'little') +
            h2.to_bytes(4, 'little') + h3.to_bytes(4, 'little')).hex()

def calculate_sha256(text):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text.encode('utf-8'))
    return sha256_hash.hexdigest()

def calculate_sha3(text):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(text.encode('utf-8'))
    return sha3_hash.hexdigest()

def calculate_blake2(text):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(text.encode('utf-8'))
    return blake2_hash.hexdigest()

class HashGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Functions GUI")
        self.resize(500, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Chọn thuật toán
        self.combo = QComboBox(self)
        self.combo.addItems([
            "SHA-256", "SHA-3", "MD5 (Library)", "MD5 (Custom)", "BLAKE2"
        ])
        self.layout.addWidget(QLabel("Chọn thuật toán băm:"))
        self.layout.addWidget(self.combo)

        # Nhập dữ liệu
        self.inputBox = QLineEdit(self)
        self.inputBox.setPlaceholderText("Nhập chuỗi cần băm...")
        self.layout.addWidget(self.inputBox)

        # Nút băm
        self.hashButton = QPushButton("Băm", self)
        self.layout.addWidget(self.hashButton)

        # Kết quả
        self.resultBox = QTextEdit(self)
        self.resultBox.setReadOnly(True)
        self.layout.addWidget(QLabel("Kết quả:"))
        self.layout.addWidget(self.resultBox)

        self.hashButton.clicked.connect(self.hash_action)

    def hash_action(self):
        text = self.inputBox.text()
        algo = self.combo.currentText()
        if not text:
            self.resultBox.setPlainText("Vui lòng nhập chuỗi cần băm.")
            return
        if algo == "SHA-256":
            result = calculate_sha256(text)
        elif algo == "SHA-3":
            result = calculate_sha3(text)
        elif algo == "MD5 (Library)":
            result = calculate_md5_library(text)
        elif algo == "MD5 (Custom)":
            result = md5_custom(text.encode('utf-8'))
        elif algo == "BLAKE2":
            result = calculate_blake2(text)
        else:
            result = "Thuật toán không hợp lệ."
        self.resultBox.setPlainText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HashGUI()
    window.show()
    sys.exit(app.exec_())