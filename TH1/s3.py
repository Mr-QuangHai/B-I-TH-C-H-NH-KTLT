print("sinh viên: Nguyễn Quang Hải")
print("MSSV: 235752021610099")
try:
    n = int(input("Nhập vào một số: "))

    if n % 2 == 0:
        print(f"Số {n} là số chẵn.")
    else:
        print(f"Số {n} là số lẻ.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")