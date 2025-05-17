def truy_cap_phan_tu(tuple_data):
    frist_element = tuple_data[0]
    last_element = tuple_data[-1]
input_tuple = eval  (input("Nhập tuple: "))
frist, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên:", frist)
print("Phần tử cuối cùng:", last)