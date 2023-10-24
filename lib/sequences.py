#!/usr/bin/env python3

def print_fibonacci(length):
    count = 0
    final = [0,1]
    temp = 0
    a = 0
    b = 1
    if length == a:
        print([])
    elif length == b:
        print([0])
    else:
        while not(count == length-2):
            temp = b + a
            a = b
            b = temp
            final.append(b)
            count = count + 1
        print(final)
    # return final
print(print_fibonacci(10))
