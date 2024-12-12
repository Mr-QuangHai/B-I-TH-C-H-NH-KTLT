
print("sinh viên: Nguyễn Quang Hải")
print("MSSV: 235752021610099")
limit = 4000000
a, b = 0, 1
even_sum = 0
print("Dãy số Fibonacci nhỏ hơn 4.000.000:")
while a < limit:
    print(a, end=' ')
    if a % 2 == 0:
        even_sum += a
    a, b = b, a + b

print("\nTổng các số chẵn trong dãy Fibonacci:", even_sum)