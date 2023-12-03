# Câu 1
A = [5, 12, 15, 7, 7, 30, 3, 56]
tong_chan = 0
for phan_tu in A:
    if phan_tu % 2 == 0:  # Kiểm tra xem phần tử có phải là số chẵn hay không
        tong_chan += phan_tu
print(f"Tổng các số chẵn trong danh sách A là: {tong_chan}")

# Câu 2
chi_tieu_ngay = []
ngay_trong_tuan = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
for i in range(7):
    chi_tieu = float(input(f"Nhập số tiền chi tiêu cho {ngay_trong_tuan[i]}: "))
    chi_tieu_ngay.append(chi_tieu)
# Tính tổng chi tiêu trong tuần
tong_chi_tieu = sum(chi_tieu_ngay)
# Tìm ngày chi tiền nhiều nhất trong tuần
ngay_nhieu_tien_nhat = ngay_trong_tuan[chi_tieu_ngay.index(max(chi_tieu_ngay))]
# Tính trung bình chi tiêu hàng ngày
trung_binh_chi_tieu = tong_chi_tieu / 7
print(f"Tổng chi tiêu trong tuần: {tong_chi_tieu} VNĐ")
print(f"Ngày chi tiền nhiều nhất trong tuần: {ngay_nhieu_tien_nhat}")
print(f"Trung bình chi tiêu hàng ngày trong tuần: {trung_binh_chi_tieu} VNĐ")

# Câu 2 - nếu có 2 ngày chi cao bằng nhau
chi_tieu_ngay = []
ngay_trong_tuan = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
for i in range(7):
    chi_tieu = float(input(f"Nhập số tiền chi tiêu cho {ngay_trong_tuan[i]}: "))
    chi_tieu_ngay.append(chi_tieu)
# Tính tổng chi tiêu trong tuần
tong_chi_tieu = sum(chi_tieu_ngay)
# Tìm ngày chi tiền nhiều nhất trong tuần
max_chi_tieu = max(chi_tieu_ngay)
ngay_nhieu_tien_nhat = [ngay for ngay, chi in zip(ngay_trong_tuan, chi_tieu_ngay) if chi == max_chi_tieu]
# Tính trung bình chi tiêu hàng ngày trong tuần
trung_binh_chi_tieu = tong_chi_tieu / 7
print(f"Tổng chi tiêu trong tuần: {tong_chi_tieu} VNĐ")
if len(ngay_nhieu_tien_nhat) == 1:
    print(f"Ngày chi tiền nhiều nhất trong tuần: {ngay_nhieu_tien_nhat[0]}")
else:
    print(f"Ngày chi tiền nhiều nhất trong tuần: {', '.join(ngay_nhieu_tien_nhat)}")
print(f"Trung bình chi tiêu hàng ngày trong tuần: {trung_binh_chi_tieu} VNĐ")

# Câu 3
loaiGiay = int(input("Nhập ký hiệu loại giấy: "))
soTrang = int(input("Số trang giấy cần in: "))
if loaiGiay == 2 and soTrang % 2 == 1:
    luong_giay_can_dung = int((soTrang / 2) + 1) 
    print("Lượng giấy cần dùng để in được tài liệu 2 mặt là: ", luong_giay_can_dung)
else: 
    if loaiGiay == 1:
        print("Lượng giấy cần dùng để in quảng cáo 1 mặt là: ", soTrang)

# Câu 4
print("*** Tính số tiền điện tiêu thụ trong tháng ***")
kwh = int(input("Nhập vào số KWH điện tiêu thụ trong tháng: "))
if kwh <= 50:
    total_amount = kwh * 1700
elif 51 <= kwh <= 100:
    total_amount = 50 * 1700 + (kwh - 50) * 1900
elif 101 <= kwh <= 200:
    total_amount = 50 * 1700 + 50 * 1900 + (kwh - 100) * 2100
else: 
    total_amount = 50 * 1700 + 50 * 1900 + 100 * 2100 + (kwh - 200) * 3000
print("Số tiền điện cần phải trả: ", total_amount, "Đồng")