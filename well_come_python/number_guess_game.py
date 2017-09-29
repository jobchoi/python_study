# -*- coding: utf-8 -*-
print("미리 저장된 숫자를 맞혀보시오.")

number = 62

user_input= input("1~100사이이의 정수를 입력하세요 \n")
input_typecast = int(user_input)

while number != input_typecast:  
    if number > input_typecast :
        print("up")
        user_input= input("재입력 1~100사이이의 정수를 입력하세요 \n")
        input_typecast = int(user_input)
    elif number <input_typecast :
        print("down")
        user_input= input("재입력 1~100사이이의 정수를 입력하세요 \n")
        input_typecast = int(user_input)
    else :
        print("저장된 값 : " + number + "\n")
        print("입력 값 : " + input_typecast + "\n")
        break
    
print("저장된 값 : ")
print(number)
print("\n")

print("저장된 값 : ")
print(input_typecast)
print(type(input_typecast))
print("\n")
