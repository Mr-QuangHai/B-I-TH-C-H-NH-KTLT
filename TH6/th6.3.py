print("Nguyễn Quang Hải")
print("Msv:235752021610099")
class Nguoi:
    def getGender(self):
        pass

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Ví dụ sử dụng
male = Nam()
female = Nu()
print("Giới tính:", male.getGender())
print("Giới tính:", female.getGender())