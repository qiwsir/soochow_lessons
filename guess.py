#coding:utf-8

import random
number = random.randint(1, 100)
flag = 0

while True:     #while flag<2:
    num_input = input("input a number(1-100):")
    flag += 1
    if not num_input.isdigit():
        print("please input a int.")
    elif int(num_input) < 0 or int(num_input) >= 100:
        print("should be in 1-100.")
    else:
        num_input = int(num_input)
        if number == num_input:
            print("good!")
            print(flag)
            break   #continue
        if number > num_input:
            print("your number is smaller.")
        else:
            print("your number is bigger.")