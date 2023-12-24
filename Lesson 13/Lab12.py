# ***Example 01***
# Tạo nội dung cho file names.txt
with open('names.txt', 'w') as file:
    file.write("Tru\n")
    file.write("Mervin Friedland\n")
    file.write("Aron Wilkins\n")    
# Đọc nội dung từ file names.txt
with open('names.txt', 'r') as file:
    lines = file.readlines()
# In ra nội dung từ file names.txt
print("List of names:")
for index, line in enumerate(lines, start=1):
    # In ra định dạng số thứ tự và tên từ file
    print(f"- {line.strip()}")

# ***Example 02***
file_name = input("Nhập tên của text file: ")

try:
    # Mở file
    with open(file_name, 'r') as file:
        # Đọc
        lines = file.readlines()
        # in
        print(f"\nFile content:")
        for index, line in enumerate(lines, start=1):
            print(f"{line.strip()}")

except FileNotFoundError:
    # In ra thông báo nếu file không tồn tại
    print(f"File {file_name} not found.")

# ***Example 03***
file_name = "user-inputs.txt"
# Viết vào file
with open(file_name, 'w') as file:
    print("Nhập nội dung vào file. Ấn Enter hai lần để kết thúc.")
    # user nhập dữ liệu
    while True:
        user_input = input("Nhập: ")
        # 2 lần enter -> thoát 
        if not user_input:
            break
        file.write(user_input + '\n')

print(f"Nội dung đã được lưu vào file {file_name}.")
# Đọc
with open(file_name, 'r') as file:
    print("Dữ liệu đã nhập từ file:")
    for line in file:
        # in
        print(line.strip())
# ***Example 05***
import random
def load_questions(file_name):
    questions = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 2:
            for i in range (0, len(lines),2):
                questions = lines[i].strip()
                answer = lines[i+1].strip()
                questions.append((questions, answer))
    return questions

def play_game(questions):
    score = 0
    random.shuffle(questions)

    for questions, correct_answer in questions:
        user_answer = input (f"\n{questions} = ")
        if user_answer.lower() == correct_answer.lower():
            print("Yess")
            score +=1
        else:
            print(f"Noo! Đáp án đúng là: {correct_answer}")

    print(f"\n Điểm của bạn: {score}/{len(questions)}")
if __name__ == "__main__":
    file_name = "question-bank.txt"
    questions = load_questions(file_name)

    if questions:
        print(f"Chào mừng bạn đến với Mini Game Trả lời Câu hỏi!")
        play_game(questions)
    else:
        print("Không có câu hỏi nào trong file.")
# code mẫu
print('Give the correct answers to get points.')
total = 0     # counts total questions
corrects = 0  # counts correct answers

with open('question-bank.txt', 'r') as fi:
  for line in fi:
    question = line.split(',')  # split line into question and answer
    print(question[0], end='')
    if input() == question[1][:-1]:  # remove '\n' from answer
      corrects += 1
    total += 1

print(f'== You get {corrects}/{total} points ==')