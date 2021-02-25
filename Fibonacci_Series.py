'''
    this script get the Fibonacci Sequence between 0 to max input 
    Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 
'''
#!/usr/bin/env python3

maximum = int(input("Please Enter The Max Value Not To Exceed : <<< "))

result = 0
previous = 1

for i in range(maximum):
    if result > maximum:
        break

    else :
        print("the fibonacci sequence number ", i,">>>>>", result)
        preofprevious = previous
        previous = result
        result = previous + preofprevious