# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:56:42 2020

@author: Nicholas Guthrie

Writing better code: Random things to remember and practice.

Future updates:
    1) rewrite using functions and classes w docstrings
        start function names with verbs
        variables should fully describe what it is
    2) use keyword arguments throughout
    3) organize related ideas into separate modules
    
"""

# to be as specific as possible
import tensorflow as tf
import tensorflow.keras as K
# will be able to use variables and functions in 
# Sequential module without preface.  

# no specificity 
import math
# vs specific
from math import log 
# in first, functions from math could overwrite functions
# in Sequential
# in the first will have to specify math.log() 

def main():
    '''
    description
    
    examples
    
    returns
    '''
    # using dir on root directory to explore docs in console
    dir(tf)
    
    # using white space without \ in python 3
    print(True and True
          or (False and False)
          or (False and True))
    
    # same spacing for lists
    L = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    
    # non-zero nums and letters are True when used as bools
    # 0 and empty string are False
    def auto_bool(value):
        if value:
            return True
        else:
            return False
    
    print(auto_bool(1))
    print(auto_bool(''))          
    
    # ternary instead of separating if, else
    covid = True
    print ("Stay home" if covid else "Go out")
    
    # eleminating True, False in ternary
    # use
    print (covid)
    # instead of
    print (True if covid else False)
    
    # can call help on specific instance
    my_model = tf.keras.Sequential()
    # help(my_model)
    
    # integer ratio for floats
    print (0.125.as_integer_ratio())
    
    # using tuples to asign and switch
    a, b = 1, 2
    a, b = b, a
    # ignoring variables with _ 
    a, _ = 1, 2
    # unpacking with catch-alls
    a, b, *c = 1, 2, 3, 4, 5
    print (c)
    
    # list comphrension
    L = [1,2,3,4,5]
    print([n**2 for n in L])
    # list comp with conditions
    print([n**2 for n in L if n**2 > 8])
    
    # using any to check if any True in array
    L1 = [True, False, False]
    print(any(L1))
    L2 = [False, False, False]
    print(any(L2))
    
    # string formatting (much more to learn)
    print ("{} is the {}st value of L1".format(L1[0], 1))
    
    #easy reading large numbers
    x = 100_000_000
    print(x)

    # enumerate
    # instead of ...
    L1 = ['a', 'b','c']
    for i in range(len(L)):
        print (i, L[i])
    # use...
    for index, value in enumerate(L):
        print (index, value)
        
    # zip to access two array-likes at the same time
    L2 = [1, 2, 3]
    for letter, number in zip(L1, L2):
        print (f'{letter} is from L1 and {number} is from L2')
    
    # defaultdict(list) vs dict
    # trying to increment d[k] when it hasn't been assigned
    # would cause an error for a regular dictionary
    # useful when using append with things that have new keys
    s = 'mississippi'
    d = defaultdict(list)
    for k in s:
        d[k] += 1
    
    
    
# setting a if __name__ == '__main__' space even when scrpting
if __name__ == '__main__':
    main()