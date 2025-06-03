#!/usr/bin/env python3

def join_lists(l1, l2):
    s1 = set(l1) #Convert l1 and l2
    s2= set(l2)  #into sets
    join = list(s1 | s2) #Convert the joined sets of s1 and s2 into a list
    return join 

def match_lists(l1, l2):
    match = list(set(l1) & set(l2)) #Combine line 4 and 5 into 1 step
    return match 

def diff_lists(l1, l2):
    diff = list(set(l1) ^ set(l2))
    return diff 

if __name__ == '__main__' : 
    list1 = list(range(1, 10))
    list2 = list(range(5, 15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))