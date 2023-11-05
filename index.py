chi_tieu_ngay = []
ngay_trong_tuan = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]


for i in range(7):
    chi_tieu = float(input(f"Nhập số tiền chi tiêu cho {ngay_trong_tuan[i]}: "))
    chi_tieu_ngay.append(chi_tieu)

# Tính tổng chi tiêu trong tuần
tong_chi_tieu = sum(chi_tieu_ngay)

# Tìm ngày chi tiền nhiều nhất trong tuần
max_chi_tieu = max(chi_tieu_ngay)
ngay_nhieu_tien_nhat = [ngay for ngay, chi in zip(ngay_trong_tuan, chi_tieu_ngay) if chi == max_chi_tieu] #[Thứ 2, Thứ 3]
# Tính trung bình chi tiêu hàng ngày trong tuần
trung_binh_chi_tieu = tong_chi_tieu / 7
print(f"Tổng chi tiêu trong tuần: {tong_chi_tieu} VNĐ")
if len(ngay_nhieu_tien_nhat) == 1:
    print(f"Ngày chi tiền nhiều nhất trong tuần: {ngay_nhieu_tien_nhat[0]}")
else:
    print(f"Ngày chi tiền nhiều nhất trong tuần: {', '.join(ngay_nhieu_tien_nhat)}")

print(f"Trung bình chi tiêu hàng ngày trong tuần: {trung_binh_chi_tieu} VNĐ")
