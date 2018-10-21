# coding:utf-8
"""
this is my first program.
coder: laoqi
date: 2018-10-14
"""
#print("Please input a int:")
#input_number = int(input("input a number:"))
input_number = input("input a number:")
if input_number.isdigit():
    input_number = int(input_number)
    if input_number > 10:
        print("more than 10")
    elif input_number < 10:
        print("less than 10")
    else:
        print("== 10")
else:
    print("babalala")
