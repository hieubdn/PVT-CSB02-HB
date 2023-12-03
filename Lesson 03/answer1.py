lst = []
c = int(input("Nhap so c"))
d = int(input("Nhap so d"))
e = int(input("Nhap so e"))
lst.append(c)
lst.append(d)
lst.append(e)
t = lst[0]
for i in range(len(lst)):
    # lst= [-5, 10, 9, -3, 4]
    if lst[i] > t:
         t = lst[i]
print(t)