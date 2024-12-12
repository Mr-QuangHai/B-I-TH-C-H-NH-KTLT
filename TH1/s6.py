print("sinh viên: Nguyễn Quang Hải")
print("MSSV: 235752021610099")
n = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        n.append(str(i))

s = ', '.join(n)
print("Các số chia hết cho 7 nhưng không phải bội số của 5 trong khoảng (2000, 3200):")
print(s)