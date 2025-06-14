import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import rsa

class RSACipher:
    def __init__(self):
        # Đường dẫn đến thư mục keys trong thư mục hiện tại
        self.key_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys')
        self.private_key_path = os.path.join(self.key_dir, 'private.pem')
        self.public_key_path = os.path.join(self.key_dir, 'public.pem')
        
        # Tạo thư mục keys nếu chưa tồn tại
        if not os.path.exists(self.key_dir):
            os.makedirs(self.key_dir)
    
    def generate_keys(self):
        """Tạo cặp khóa RSA mới và lưu vào file"""
        (pubkey, privkey) = rsa.newkeys(2048)
        
        # Lưu khóa riêng tư
        with open(self.private_key_path, 'wb') as f:
            f.write(privkey.save_pkcs1())
        
        # Lưu khóa công khai
        with open(self.public_key_path, 'wb') as f:
            f.write(pubkey.save_pkcs1())
        
        return privkey, pubkey
    
    def load_keys(self):
        """Đọc khóa RSA từ file"""
        try:
            with open(self.private_key_path, 'rb') as f:
                private_key = rsa.PrivateKey.load_pkcs1(f.read())
            
            with open(self.public_key_path, 'rb') as f:
                public_key = rsa.PublicKey.load_pkcs1(f.read())
            
            return private_key, public_key
        except FileNotFoundError:
            # Tạo khóa mới nếu chưa tồn tại
            return self.generate_keys()
    
    def encrypt(self, message, key):
        """Mã hóa tin nhắn bằng RSA"""
        message_bytes = message.encode('utf-8')
        return rsa.encrypt(message_bytes, key)
    
    def decrypt(self, ciphertext, key):
        """Giải mã tin nhắn bằng RSA"""
        try:
            decrypted = rsa.decrypt(ciphertext, key)
            return decrypted.decode('utf-8')
        except:
            return "Giải mã thất bại. Hãy đảm bảo bạn đang sử dụng đúng khóa."
    
    def sign(self, message, private_key):
        """Ký tin nhắn bằng khóa riêng tư RSA"""
        message_bytes = message.encode('utf-8')
        signature = rsa.sign(message_bytes, private_key, 'SHA-1')
        return signature
    
    def verify(self, message, signature, public_key):
        """Xác minh chữ ký bằng khóa công khai RSA"""
        message_bytes = message.encode('utf-8')
        try:
            rsa.verify(message_bytes, signature, public_key)
            return True
        except:
            return False

class RSAApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.rsa_cipher = RSACipher()
        
        # Kết nối các nút với các hàm tương ứng
        self.ui.btn_gen_keys.clicked.connect(self.generate_keys)
        self.ui.btn_encrypt.clicked.connect(self.encrypt)
        self.ui.btn_decrypt.clicked.connect(self.decrypt)
        self.ui.btn_sign.clicked.connect(self.sign)
        self.ui.btn_verify.clicked.connect(self.verify)
    
    def generate_keys(self):
        try:
            self.rsa_cipher.generate_keys()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Tạo khóa thành công")
            msg.exec_()
        except Exception as e:
            self.show_error(f"Lỗi khi tạo khóa: {str(e)}")
    
    def encrypt(self):
        try:
            message = self.ui.txt_plain_text.toPlainText()
            if not message:
                self.show_error("Vui lòng nhập văn bản để mã hóa")
                return
                
            _, public_key = self.rsa_cipher.load_keys()
            encrypted = self.rsa_cipher.encrypt(message, public_key)
            encrypted_hex = encrypted.hex()
            
            self.ui.txt_cipher_text.setPlainText(encrypted_hex)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Mã hóa thành công")
            msg.exec_()
        except Exception as e:
            self.show_error(f"Lỗi mã hóa: {str(e)}")
    
    def decrypt(self):
        try:
            ciphertext_hex = self.ui.txt_cipher_text.toPlainText()
            if not ciphertext_hex:
                self.show_error("Vui lòng nhập văn bản mã hóa để giải mã")
                return
                
            private_key, _ = self.rsa_cipher.load_keys()
            ciphertext = bytes.fromhex(ciphertext_hex)
            decrypted = self.rsa_cipher.decrypt(ciphertext, private_key)
            
            self.ui.txt_plain_text.setPlainText(decrypted)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Giải mã thành công")
            msg.exec_()
        except ValueError:
            self.show_error("Định dạng hex không hợp lệ trong văn bản mã hóa")
        except Exception as e:
            self.show_error(f"Lỗi giải mã: {str(e)}")
    
    def sign(self):
        try:
            message = self.ui.txt_info.toPlainText()
            if not message:
                self.show_error("Vui lòng nhập thông tin để ký")
                return
                
            private_key, _ = self.rsa_cipher.load_keys()
            signature = self.rsa_cipher.sign(message, private_key)
            signature_hex = signature.hex()
            
            self.ui.txt_sign.setPlainText(signature_hex)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Ký thành công")
            msg.exec_()
        except Exception as e:
            self.show_error(f"Lỗi ký: {str(e)}")
    
    def verify(self):
        try:
            message = self.ui.txt_info.toPlainText()
            signature_hex = self.ui.txt_sign.toPlainText()
            
            if not message or not signature_hex:
                self.show_error("Vui lòng nhập cả thông tin và chữ ký")
                return
                
            _, public_key = self.rsa_cipher.load_keys()
            signature = bytes.fromhex(signature_hex)
            is_verified = self.rsa_cipher.verify(message, signature, public_key)
            
            msg = QMessageBox()
            if is_verified:
                msg.setIcon(QMessageBox.Information)
                msg.setText("Xác minh thành công")
            else:
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Xác minh thất bại")
            msg.exec_()
        except ValueError:
            self.show_error("Định dạng hex không hợp lệ trong chữ ký")
        except Exception as e:
            self.show_error(f"Lỗi xác minh: {str(e)}")
    
    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RSAApp()
    window.show()
    sys.exit(app.exec_())