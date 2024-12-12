print("sinh viên: Nguyễn Quang Hải")
print("MSSV: 235752021610099")
try:
    n = int(input("Nhập vào một số tự nhiên n (n > 0): "))

    if n <= 0:
        print("Vui lòng nhập một số tự nhiên lớn hơn 0.")
    else:
        print("Các số tự nhiên giảm dần từ n đến 0:")
        for i in range(n, -1, -1):
            print(i)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")