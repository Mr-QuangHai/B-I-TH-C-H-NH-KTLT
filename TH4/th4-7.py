print("Nguyễn Quang Hải")
print("Msv:235752021610099")
chuoi = input("Nhập chuỗi: ")
chuoi_khong_chu_so = ''.join([char for char in chuoi if not char.isdigit()])
print(chuoi_khong_chu_so)