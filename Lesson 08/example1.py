# Khai báo dictionary biểu diễn thông tin về số lượng máy tính
computer_inventory = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

# Hiển thị số lượng MACBOOK có trong kho
print("Số lượng MACBOOK có trong kho:", computer_inventory['MACBOOK'])

# Đọc số lượng máy tính theo hãng nhập từ người dùng
brand_input = input("Nhập hãng máy tính cần kiểm tra: ")

# Kiểm tra xem hãng nhập vào có trong dictionary hay không
if brand_input in computer_inventory:
    quantity = computer_inventory[brand_input]
    print(f"Số lượng {brand_input} có trong kho: {quantity}")
else:
    print(f"Không có thông tin về số lượng máy tính của hãng {brand_input} trong kho.")
