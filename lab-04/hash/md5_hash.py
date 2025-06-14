# md5_hash.py

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length = len(message)
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    # Chia chuỗi thành các khối 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]
        
        a0, b0, c0, d0 = h0, h1, h2, h3
        
        # Vòng lặp chính của thuật toán MD5
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
        
    return (h0.to_bytes(4, 'little') + h1.to_bytes(4, 'little') + h2.to_bytes(4, 'little') + h3.to_bytes(4, 'little')).hex()

input_string = input("Nhập chuỗi cần băm: ")
md5_hash_output = md5(input_string.encode('utf-8'))

print(f"MD5 hash của chuỗi '{input_string}' là: {md5_hash_output}")