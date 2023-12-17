def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

# Kiểm thử
chuoi = input("Nhập một chuỗi: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(chuoi))