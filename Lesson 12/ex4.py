def la_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def loc_so_nguyen_to(danh_sach):
    so_nguyen_to = [x for x in danh_sach if la_so_nguyen_to(x)]
    return so_nguyen_to

danh_sach_so = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Danh sách gốc:", danh_sach_so)
ket_qua = loc_so_nguyen_to(danh_sach_so)
print("Danh sách chỉ chứa số nguyên tố:", ket_qua)
