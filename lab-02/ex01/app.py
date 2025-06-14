from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()
vigenere_cipher = VigenereCipher()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return render_template('caesar.html', result=f"Encrypted: {encrypted_text}")

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return render_template('caesar.html', result=f"Decrypted: {decrypted_text}")

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    key = request.form['inputKey']
    plain_text = request.form['inputPlainText']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return render_template('playfair.html', matrix=matrix, result=encrypted_text)

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    key = request.form['decryptKey']
    cipher_text = request.form['inputCipherText']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return render_template('playfair.html', matrix=matrix, result=decrypted_text)

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    rails = int(request.form['inputRails'])
    plain_text = request.form['inputPlainText']
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, rails)
    return render_template('railfence.html', result=encrypted_text)

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    rails = int(request.form['decryptRails'])
    cipher_text = request.form['inputCipherText']
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, rails)
    return render_template('railfence.html', result=decrypted_text)

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    key = int(request.form['inputKey'])
    plain_text = request.form['inputPlainText']
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return render_template('transposition.html', result=encrypted_text)

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    key = int(request.form['decryptKey'])
    cipher_text = request.form['inputCipherText']
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return render_template('transposition.html', result=decrypted_text)

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    key = request.form['inputKey']
    plain_text = request.form['inputPlainText']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return render_template('vigenere.html', result=encrypted_text)

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    key = request.form['decryptKey']
    cipher_text = request.form['inputCipherText']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return render_template('vigenere.html', result=decrypted_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)