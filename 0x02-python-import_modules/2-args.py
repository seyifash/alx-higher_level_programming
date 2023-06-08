#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    num_args = len(arg) - 1
    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))
        print("{}: {}".format(num_args, arg[1]))
    else:
        print("{} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, arg[i]))
