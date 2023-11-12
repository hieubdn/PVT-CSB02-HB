# Hàm zip trong Python được sử dụng để kết hợp các phần tử từ nhiều danh sách(iterables) 
# thành các cặp hoặc bộ dữ liệu dựa trên thứ tự của chúng
# ví dụ:
ngay_trong_tuan = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm"]
chi_tieu_ngay = [100, 200, 150, 300]
# Sử dụng zip để kết hợp hai danh sách thành các cặp (ngay, chi_tieu)
for ngay, chi in zip(ngay_trong_tuan, chi_tieu_ngay):
    print(f"{ngay}: {chi} VNĐ")