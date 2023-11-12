# Tính tổng số chẳn từ 0 đến n
n = int(input("nhap n: "))
sum = 0
for i in range(0, n+1):
    if i % 2 == 0:
        sum = sum + i
        i = i+1
print(sum)