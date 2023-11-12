import random
print("== FREAKING MATH CONSOLE ==")
print("Give correct answers to get scores.")

symbol = ['+', '-', '*', '/']
total_score = 0

player = True
while True:

    a = random.randint(-10,10)
    b = random.choice(symbol)
    c = random.randint(-10,10)
    d = random.randint(-100,100)

    print(a,b,c,"=",d)
    answer = input("1 for True, 0 for False: ")
    question = '1'
    # Kiểm tra tính đúng sai của phep tính
    if b == '+':
        if a + c == d:
            question = '1'
        else:
            question = '0'
    if b == '-':
        if a - c == d:
            question = '1'
        else:
            question = '0'
    if b == '*':
        if a * c == d:
            question = '1'
        else:
            question = '0'
    if b == '/':
        if a / c == d:
            question = '1'
        else:
            question = '0'

    # Kiểm tra đáp án của người chơi
    if answer == question:
        total_score +=1
        print("score: ",total_score)
    else:
        break

print("== GAME OVER ==")
print("Your total score is", total_score)