''' Artem Lecture CSPT 8 '''


###
'''
To Analyze:
Step 1. Does the number of steps increase if the input size increases?
Step 2. Go line by line. Figure out what Big-O of each line is and add them.
Step 3. If dealing with loop: look at code inside and repeat Step 2.
Step 4. If dealing with loop: calculate number of times will run.
Step 5. If dealing with loop: multiply the result of Step 3 by Step 4

'''

import math
from math import sqrt

# CONSTANT runtime O(1) or O(c)
# Step 1. = No
# Step 2. this whole function is O(1) + O(1) + O(1) + O(1) = O(4) => O(1)

def mult_2(n): # O(1) + O(1) + O(1) + O(1) = O(4) ==> O(1)
    print(n) # O(1)
    if n == 5: # O(1)
        print('Bingo') # O(1)
    return n * 2 # O(1)


# LINEAR TIME O(n)
# evaluate Big O for a loop
# Step 5. this whole loop runtime is  O(n)

def foo(n):
    for i in range(0, n): # O(n)

        # total time for code inside loop is O(1) + O(1) = O(2) ==> O(1)
        print(i) # O(1)
        print(i) # O(1)

#
# nested for loops runtime is QUADRATIC/POLYNOMIAL TIME

def bar(n): # O(1) + O(n^2) +O(1) {simplify to worst runtime} ==> O(n^2)
    s = 0 # O(1)
    
    # i loop is EXPONENTIAL TIME
    for i in range(0, n): # O(n) * O(n){j loop} = O(n^2)
        # j loop is LINEAR TIME
        for j in range(0, n): # O(n) * O(1){s code below} = O(n)
            s += i * j # O(1) + O(1) = O(2) ==> O(1)

    return s # O(1)


#
# SQUARE ROOT N TIME or variant of (O(n) * log(n))

def baz(n): # O(n) * O(sqrt(n)) == O(n * sqrt(n)) ==> O(n^1.5)
    s = 0

    for i in range(n): # O(n)
        for j in range(int(sqrt(n))): # O(sqrt(n)) or O(n^0.5)
            s += i * j # O(1)

    return s

#
# LOGARITHMIC TIME

def divider(n): # whole function summed up and the worst time is O(log(n))
    while n >= 1: # O(log(n))
        print(n) # O(1)
        n = n // 2 # O(1) usualy division == LOGARITHMIC TIME
    
    return n # O(1)


