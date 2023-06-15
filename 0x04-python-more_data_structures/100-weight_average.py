#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    wssum = 0
    weightsum = 0
    for tup in my_list:
        wssum += tup[0] * tup[1]
        weightsum += tup[1]
    return wssum / weightsum
