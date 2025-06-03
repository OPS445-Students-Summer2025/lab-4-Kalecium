#!/usr/bin/env python3

def join_sets(s1, s2):
    join = s1 | s2 #combine 2 sets
    return join 

def match_sets(s1, s2):
    match = s1 & s2
    return match 

def diff_sets(s1, s2):
    diff = s1 ^ s2
    return diff 

if __name__ == '__main__' : 
    set1 = set(range(1, 10))
    set2 = set(range(5, 15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))