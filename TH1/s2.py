print("sinh viên: Nguyễn Quang Hải")
print("MSSV: 235752021610099")
try:
    n1 = int(input("Enter n1 value: "))
    n2 = int(input("Enter n2 value: "))

    if n1 > n2:
        print("n1 is big")
    elif n1 < n2:
        print("n2 is big")
    else:
        print("n1 and n2 are equal")
except ValueError:
    print("Please enter valid integers.")
 