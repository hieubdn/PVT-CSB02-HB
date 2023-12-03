def reverse_str(input_str):
    """Hàm đảo ngược một chuỗi."""
    return input_str[::-1]
# [start : stop : step]
user_input = input("Nhập chuỗi cần đảo ngược: ")

# Sử dụng hàm reverse_str() để đảo ngược chuỗi
reversed_input = reverse_str(user_input)
print("Chuỗi sau khi đảo ngược:", reversed_input)
