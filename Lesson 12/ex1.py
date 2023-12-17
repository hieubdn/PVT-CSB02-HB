def tinh_tong(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    return tong

n = int(input("Nhập một số nguyên dương n: "))
print("Tổng các số từ 1 đến", n, "là:", tinh_tong(n))