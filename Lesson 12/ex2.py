def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

so = int(input("Nhập một số nguyên dương: "))
if la_so_nguyen_to(so):
    print(so, "là số nguyên tố.")
else:
    print(so, "không là số nguyên tố.")
