print("sinh viên: Nguyễn Quang Hải")
print("MSSV: 235752021610099")
n = int(input("Nhập vào một số nguyên n: "))
if n < 1:
        print("Vui lòng nhập một số nguyên lớn hơn hoặc bằng 1.")
else:
        s = {i: i * i for i in range(1, n + 1)}
        print("Dictionary chứa các cặp (i, i*i):",s)
      