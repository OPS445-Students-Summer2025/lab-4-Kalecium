#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string1):
    return string1[0:5]

def last_seven(string2):
    return string2[-7:]

def middle_number(numbr):
    out = str(numbr)
    return out[1:3]

def first_three_last_three(str1, str2):
    return str1[0:3] + str2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))