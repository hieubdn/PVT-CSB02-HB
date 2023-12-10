print('Input a number: ', end='')
num = int(input())

count = 0
while num > 0:
  count += 1
# Loại bỏ chữ số cuối cùng của num bằng cách chia num cho 10 và lấy phần nguyên.
  num //= 10  

print(f'This number has {count} digit(s).')