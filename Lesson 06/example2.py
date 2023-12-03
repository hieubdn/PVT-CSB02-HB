# Bài 2:
s = input("Nhập vào ngày tháng năm (dd/mm/yyyy): ")
result = "Ngày "  + s # Ngày dd/mm/yyyy
result = result.replace('/', ' tháng ', 1) # Ngày dd tháng mm/yyyy
result = result.replace('/', ' năm ') # Ngày dd tháng mm năm yyyy
print(result)