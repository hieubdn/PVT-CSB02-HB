
nam = int(input("nam nhuan :   "))

if nam % 4 ==0 :
    if nam % 100 == 0 and nam % 400 == 0 :
        print("nam nhuan")
    elif nam % 100 == 0 and nam % 400 != 0 :
        print("ko phai nam nhuan")
    else :
        print("nam nhuan")
else:
    print("khong phai nam nhuan")