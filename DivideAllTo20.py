# The smallest natural number that is divisible by all digits 1-10 is 2520.
# This script will find the smallest number that divides all digits 1-20.

def check(x, NumList):
    t = 0
    for element in NumList:
        if x%element == 0:
            t += 1
            if t == len(NumList):
                print('{} is correct'.format(x))
                return x
            else:
                continue
        else:
            #print('{} is not divisible by {}.'.format(x, element))
            t = 0
            return x
x=2520
List20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
while True:
    x = check(x, List20)
    x+=20
