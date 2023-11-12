# Bài 1: Viết chương trình nhập vào họ và tên người dùng, và xuất ra họ của người đó
ho_ten = input("Nhập họ và tên: ")
vi_tri_khoang_trang_dau_tien=ho_ten.find(' ')
ho = ''
for i in range(vi_tri_khoang_trang_dau_tien):
    ho += ho_ten[i] 
print("Họ của người bạn là:", ho)