#Khai báo biến.
x=10
name="Alice"
is_valid= True

#Từ khoá
#if = 5 
#lỗi hiển thị vì if không phải biến mà là từ khoá.

#Toán từ cộng giữa hai số.
a = 5
b = 3
resulf = a + b
#Kết quả = 8. a, b, resulf là biến.

#Toán tử trừ giữa hai số.
a = 8
b = 4
resulf = a - b
# Kết quả = 4.

#Toán từ nhân giữa hai số.
a = 6
b = 7 
resulf = a * b
#Kết quả = 42.

#Toán tử chia giữa hai số.
a = 20
b = 5
resulf = a / b
#Kết quả = 4.0(Kết quả phép chia luôn là số thập phân)

#Toán từ chia lấy phần nguyên. Kết quả trả về luôn là phần nguyên của phép chia.
a = 20
b = 3
resulf = a // b
#Kết quả = 6.

#Toán tử chia lấy phần dư. Kết quả trả về luôn là phần dư của phép chia
a = 20
b = 7
resulf = a % b
#Kết quả = 6 (Phần dư của 20 / 7).

#Toán tử luỹ thừa
a = 2 
b = 3
resulf = a ** b
#Kết quả = 8 (2^3 = 8).

#Phép toán "and" trả về "True" nếu cả hai điều kiện đều đúng.
x = 5
y = 3
resulf = (x>2) and (y<4)
#Kết quả = True.

#Phép toán "or" trả về "True" nếu một trong hai điều kiện có kết quả trả về là đúng.
x = 5
y = 3
resulf = (x>2) or (y>4)
#Kết quả = True (x = 5 > 2).

#Phép toán "not" trả về "True" nếu điều kiện là "Flase" và ngược lại.
x = 5
#Kết quả = Flase.

#Phép toán so sách "==" so sách giữa hai giá trị bằng nhau.
x = 5
resulf = not (x == 5)
#Kết quả = True.

#Phép toán so sách "!=" so sách giữa hai giá trị không bằng nhau.
x = 5
resulf = (x != 3)
#Kết quả = True.

#Phép toán so sách lớn hơn ">" nhỏ hơn "<" .
x = 5
resulf1 = (x > 2) #so sánh lớn hơn #Kết quả = True.
resulf2 = (x < 3) #so sánh nhỏ hơn #Kết quả = Flase.

#Phép toán lớn hơn hoặc bằng ">=" nhỏ hơn hoặc bằng "<="
x = 5
resulf1 = (x >= 3) #so sánh lớn hơn hoặc bằng #Kết quả = True.
resulf2 = (x <= 3) #so sánh nhỏ hơn hoặc bằng #Kết quả = Flase.

#Nhập xuất dữ liệu.
#VD1:
name = input("Nhập tên của bạn: ")
print("Xin chào,",name)
#VD2:
age = 21
print("Tuổi của bạn là:",age)
#input dùng để nhập dữ liệu từ bàn phím.
#print dùng để xuất dữ liệu từ bàn phím.

#Định dạng hiển thị "sep" (ký tự phân cách), "end" (ký tự kết thúc).
print("Ngon", "ngu", "lap","trinh","Python",sep="-")
#Kết quả = Ngon-ngu-lap-trinh-Python
print("Xin chao", end=" ")
print("các bạn!")
#Kết quả = Xin chao các bạn!

#Câu lệnh điều kiện (Conditional Statements): "if", "else", "elif"(else if).
x = 10
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")
#Kết quả = x lớn hơn 5.

#Vòng lặp "Loops" hai loại vòng lọc phổ biến là "for" và "while" và "pass".
#Vòng lặp "for" dùng để duyệt qua một chuỗi hoặc một tập hợp các phần tử.
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
#Vòng lặp "while" thực hện việc lặp lại mã đến khi điều kiện không còn đúng nữa.
count = 0
while count < 5:
    print(count)
    count+=1

#Câu lệnh nhảy(Jump Statements) dùng để thay đổi luồng của tiến trình. Các câu lệnh nhảy phổ biến.
#Sử dụng câu lệnh "break" để kết thúc một vòng lặp.
for i in range(1,101):
    if i % 5 == 0:
        print("Số chia hết cho 5 đầu tiên là: ",i)
        break
#Sử dụng câu lệnh "continue" được dùng để bỏ qua vòng lặp hiện tại qua vòng lặp tiếp theo. 
for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)
#Sử dụng câu lệnh "pass" như một tuyên bố rỗng.
x = 5
if x > 10:
    print("x lớn hơn 10")
else:
    pass
#Kiểm tra điều kiện đúng thì thực hiện nếu sai thì không làm gì.

#Khai báo chuỗi.
string_single_quotes = 'Đây là một chuỗi trong dấu ngoặc đơn.'
string_double_quotes = "Đây là một chuỗi nằm trong dấu ngoặc kép."
string_triple_quotes = '''Đây là một chuỗi 
sử dụng dấu ngoặc ba
có thể trải dài qua nhiều dòng.'''

#Truy cập ký tự trong chuỗi.
my_string = "Hello, World!"
print(my_string[0]) #Kết quả: 'H'.
print(my_string[7]) #Kết quả: 'W'.

#Cắt chuỗi:
my_string = "Hello, World!"
print(my_string[7:]) #Lấy ký tự từ thứ 7 đến hết: Kết quả: 'World!'.
print(my_string[:5]) #Lấy ký tự đầu đến ký tự 4: Kết quả: 'Hello'.
print(my_string[3:8]) #Lấy ký tự 3 đến ký tự 7: Kết quả: 'lo, W'.

#Ghép chuỗi 
string = "Hello"
strings = "Hien"
concactenated_string = string + " " + strings
#Kết quả = Hello Hien.
    
#Tính độ dài chuỗi hàm "len()".
string = "tran hien"
lenght = len(string) 
#Kết quả = 9.

#Một số hàm dùng để xử lý chuỗi
#=========================================#
#Một số hàm dùng để xử lý chuỗi
#upper(): Chuyển đổi thành ký tự hoa
string = 's ,ddd'
print(string.upper())
#Kết quả: 'S, DDD'

#lower(): Chuyển đổi thành ký tự thường
string = 'S ,dDD'
print(string.lower())
#Kết quả: 's, ddd'

#strip(): Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
string1 ="    Hi,ww!   "
print(string.strip())
#Kết quả: 'Hi,w!'

#split(): Phân tách chuỗi thành danh sách các từ hoặc phần tử.
string = "Hi, Hien"
print(string.split(","))
#Kết quả: ['Hi', [Hien]]

#replace(): Thay thế một phần của chuỗi bằng một chuỗi khác.
string = "hi, hien"
print(string.replace("hi","hello"))
#Kết quả: 'hello, hien'
#=========================================#

#Hàm (function)
#Khai báo hàm sử dụng từ khoá "def" - tên hàm và danh sách tham số(nếu có).


