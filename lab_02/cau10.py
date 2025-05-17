def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_str = input("Nhập chuỗi: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_str))