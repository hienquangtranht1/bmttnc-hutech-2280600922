from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSignal, Qt
import sys
import socket
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import threading

class ChatClient(threading.Thread):
    message_received = None  # Sẽ được gán từ ChatWindow

    def __init__(self, host, port):
        super().__init__(daemon=True)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.client_key = RSA.generate(2048)
        self.server_public_key = RSA.import_key(self.client_socket.recv(2048))
        self.client_socket.send(self.client_key.publickey().export_key(format='PEM'))
        self.aes_key = self.receive_aes_key()
        self.running = True

    def receive_aes_key(self):
        encrypted_aes_key = self.client_socket.recv(1024)
        cipher_rsa = PKCS1_OAEP.new(self.client_key)
        return cipher_rsa.decrypt(encrypted_aes_key)

    def encrypt_message(self, message):
        cipher = AES.new(self.aes_key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
        return cipher.iv + ciphertext

    def decrypt_message(self, encrypted_message):
        iv = encrypted_message[:AES.block_size]
        ciphertext = encrypted_message[AES.block_size:]
        cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_message.decode()

    def run(self):
        while self.running:
            try:
                encrypted_message = self.client_socket.recv(1024)
                if not encrypted_message:
                    break
                decrypted_message = self.decrypt_message(encrypted_message)
                if self.message_received:
                    self.message_received.emit(f"Server: {decrypted_message}")
            except Exception:
                break

    def send_message(self, message):
        encrypted_message = self.encrypt_message(message)
        self.client_socket.send(encrypted_message)

    def close(self):
        self.running = False
        self.client_socket.close()

from PyQt5.QtCore import pyqtSignal

class ChatWindow(QWidget):
    message_received = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat UI")
        self.resize(400, 500)

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Khung chat
        self.chatBox = QTextEdit(self)
        self.chatBox.setReadOnly(True)
        self.layout.addWidget(self.chatBox)

        # Ô nhập tin nhắn
        self.inputBox = QLineEdit(self)
        self.layout.addWidget(self.inputBox)

        # Nút gửi
        self.sendButton = QPushButton("Gửi", self)
        self.layout.addWidget(self.sendButton)

        # Sự kiện nút gửi
        self.sendButton.clicked.connect(self.send_message)
        self.inputBox.returnPressed.connect(self.send_message)

        # Client
        self.client = ChatClient('localhost', 12345)
        self.message_received.connect(self.show_message)
        self.client.message_received = self.message_received
        self.client.start()

    def show_message(self, message):
        self.chatBox.append(message)

    def send_message(self):
        message = self.inputBox.text().strip()
        if message:
            self.client.send_message(message)
            self.show_message(f"Bạn: {message}")
            self.inputBox.clear()

    def closeEvent(self, event):
        self.client.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())