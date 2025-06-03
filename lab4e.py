#!/usr/bin/env python3
# Author ID: 150563211

def is_digits(sobj):
    result = False 
    non_digit_count = 0 #Counter for non digit characters
    for char in sobj: #Loop through each character of sobj
        if char not in '0123456789': #Check if char is not a digit
            non_digit_count = non_digit_count + 1 #Add 1 to the not digit counter
    if non_digit_count == 0: #If there's no non digit character
        result = True #return True
    return result

#I know that not in might not be in the scope of what was taught so I'm going to offer
#a previous iteration 
# def is_digits(sobj):
#     result = False 
#     digit_count = 0 #Digit characters counter
#     for char in sobj: #Loop through each character of sobj
#         if char in '0123456789': #Check if char is not a digit
#             digit_count = digit_count + 1 #Add 1 to the digit counter
#     if digit_count == len(sobj): #If the number digit characters is equal
#         result = True #to the number of characters in the sobj return True
#     return result


if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')