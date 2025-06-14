import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import rsa
import os
import base64

class RSACipher:
    def __init__(self):
        self.key_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys')
        self.private_key_path = os.path.join(self.key_dir, 'private.pem')
        self.public_key_path = os.path.join(self.key_dir, 'public.pem')
        
        # Create keys directory if it doesn't exist
        if not os.path.exists(self.key_dir):
            os.makedirs(self.key_dir)
    
    def generate_keys(self):
        """Generate a new RSA key pair and save to files"""
        (pubkey, privkey) = rsa.newkeys(2048)
        
        # Save private key
        with open(self.private_key_path, 'wb') as f:
            f.write(privkey.save_pkcs1())
        
        # Save public key
        with open(self.public_key_path, 'wb') as f:
            f.write(pubkey.save_pkcs1())
        
        return privkey, pubkey
    
    def load_keys(self):
        """Load RSA keys from files"""
        try:
            with open(self.private_key_path, 'rb') as f:
                private_key = rsa.PrivateKey.load_pkcs1(f.read())
            
            with open(self.public_key_path, 'rb') as f:
                public_key = rsa.PublicKey.load_pkcs1(f.read())
            
            return private_key, public_key
        except FileNotFoundError:
            # Generate keys if they don't exist
            return self.generate_keys()
    
    def encrypt(self, message, key):
        """Encrypt a message using RSA"""
        message_bytes = message.encode('utf-8')
        return rsa.encrypt(message_bytes, key)
    
    def decrypt(self, ciphertext, key):
        """Decrypt a message using RSA"""
        try:
            decrypted = rsa.decrypt(ciphertext, key)
            return decrypted.decode('utf-8')
        except:
            return "Decryption failed. Make sure you're using the correct key."
    
    def sign(self, message, private_key):
        """Sign a message using RSA private key"""
        message_bytes = message.encode('utf-8')
        signature = rsa.sign(message_bytes, private_key, 'SHA-1')
        return signature
    
    def verify(self, message, signature, public_key):
        """Verify a signature using RSA public key"""
        message_bytes = message.encode('utf-8')
        try:
            rsa.verify(message_bytes, signature, public_key)
            return True
        except:
            return False

class StandaloneRSAApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.rsa_cipher = RSACipher()
        
        # Connect buttons to functions
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
            msg.setText("Keys generated successfully")
            msg.exec_()
        except Exception as e:
            self.show_error(f"Error generating keys: {str(e)}")
    
    def encrypt(self):
        try:
            message = self.ui.txt_plain_text.toPlainText()
            if not message:
                self.show_error("Please enter text to encrypt")
                return
                
            _, public_key = self.rsa_cipher.load_keys()
            encrypted = self.rsa_cipher.encrypt(message, public_key)
            encrypted_hex = encrypted.hex()
            
            self.ui.txt_cipher_text.setPlainText(encrypted_hex)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Encrypted Successfully")
            msg.exec_()
        except Exception as e:
            self.show_error(f"Encryption error: {str(e)}")
    
    def decrypt(self):
        try:
            ciphertext_hex = self.ui.txt_cipher_text.toPlainText()
            if not ciphertext_hex:
                self.show_error("Please enter ciphertext to decrypt")
                return
                
            private_key, _ = self.rsa_cipher.load_keys()
            ciphertext = bytes.fromhex(ciphertext_hex)
            decrypted = self.rsa_cipher.decrypt(ciphertext, private_key)
            
            self.ui.txt_plain_text.setPlainText(decrypted)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Decrypted Successfully")
            msg.exec_()
        except ValueError:
            self.show_error("Invalid hex format in ciphertext")
        except Exception as e:
            self.show_error(f"Decryption error: {str(e)}")
    
    def sign(self):
        try:
            message = self.ui.txt_info.toPlainText()
            if not message:
                self.show_error("Please enter information to sign")
                return
                
            private_key, _ = self.rsa_cipher.load_keys()
            signature = self.rsa_cipher.sign(message, private_key)
            signature_hex = signature.hex()
            
            self.ui.txt_sign.setPlainText(signature_hex)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Signed Successfully")
            msg.exec_()
        except Exception as e:
            self.show_error(f"Signing error: {str(e)}")
    
    def verify(self):
        try:
            message = self.ui.txt_info.toPlainText()
            signature_hex = self.ui.txt_sign.toPlainText()
            
            if not message or not signature_hex:
                self.show_error("Please enter both information and signature")
                return
                
            _, public_key = self.rsa_cipher.load_keys()
            signature = bytes.fromhex(signature_hex)
            is_verified = self.rsa_cipher.verify(message, signature, public_key)
            
            msg = QMessageBox()
            if is_verified:
                msg.setIcon(QMessageBox.Information)
                msg.setText("Verified Successfully")
            else:
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Verification Failed")
            msg.exec_()
        except ValueError:
            self.show_error("Invalid hex format in signature")
        except Exception as e:
            self.show_error(f"Verification error: {str(e)}")
    
    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StandaloneRSAApp()
    window.show()
    sys.exit(app.exec_())
