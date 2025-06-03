#!/usr/bin/env python3

dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    count = 0     #Counter for list_values indexes
    temp = dict() #Create temporary dictionary
    for key in keys:    #For loop going through every entry in list_key
        temp[key] = values[count]   
        #For each key in keys list, assign a value to it from values list
        #with the index value equal to count
        count = count + 1 
        #Increase the value of count
        #so all entries in values while be assigned after each loop
    return temp 

def shared_values(d1, d2):
    share = set(d1.values()) & set(d2.values())
    #Convert d1 and d2 values into sets
    #then create a set of commons between the 2 
    return share 

york = create_dictionary(list_keys, list_values)
print('York: ', york)
common = shared_values(dict_york, dict_newnham)
print('Shared Values', common)

