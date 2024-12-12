print("sinh viên: Nguyễn Quang Hải")
print("MSSV: 235752021610099")
input_string = input("Nhập vào một xâu ký tự: ")
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1  # Tăng số lần xuất hiện
    else:
        char_count[char] = 1  # Khởi tạo số lần xuất hiện

print("Số ký tự trong xâu và số lần xuất hiện:",char_count)