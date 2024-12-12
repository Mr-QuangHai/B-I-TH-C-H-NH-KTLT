print("sinh viên: Nguyễn Quang Hải")
print("MSSV: 235752021610099")
j=[]
for i in range (2000,3021):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (','.join(j))
