#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set(my_list)
    sum_uniq = 0
    for num in uniq_num:
        sum_uniq += num
    return sum_uniq
