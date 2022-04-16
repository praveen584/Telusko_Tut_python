# print(2+3)
# print(2-3)
# print(2*3)
# print(4//2)
# print((2+3)*2)
# print(2**2)
# print(10%3)

# a = 'print'
# print(a)
# print("Tejas's laptop")
# print('Tejas "laptop"')
# print('Tejas\'s "laptop"')
# print(a+a)
# print(a*2)
# print('c:\doc\tejas')
# print(r'c:\doc\tejas')

# a = 2
# a = 3
# b = a+3
# q = _+4
# print(_+2)

# s = 'amazon'
# print(s+' flipkart')
# print(s[0])
# print(s[5])
# print(s[-1])
# print(s[-1])
# print(s[-1])
# print(s[2:10])
# s[1] = 'my' # Not allowed as it is immutable
# print('using '+s)
# print(len(s))

# a = 10
# c = 12
# b = a
# print(id(a),id(c))
# print(id(a),id(c))
# print(a is c)

# print(id(a),id(b))
# print(a is b)

# a= 1.2
# print(type(a))
# n= 3
# print(type(n))
# n= 3+8j
# print(type(n))
# b = int(a)
# print(b,type(b))
# b = complex(int(a),n)
# print(b,type(b))
# print( n < int(a) )
# non = None
# r = range(5)
# print(r,type(r),non)

# print(list(range(10)))
# print(tuple(range(10)))
# print(set(range(10)))
# print(list(range(2,10,2)))
# d = {'a':1,'b':2}
# print(list(d.keys()))

# import math 
# x = math.sqrt(25)
# y = math.sqrt(15)
# c = math.floor(1.5)
# f = math.ceil(1.5)
# p = math.pow(2,2)
# print(x,y,c,f,p,sep=' ,')

# print(int(math.sqrt(4)))

# x = int(input('Enter a value: '))
# y = int(input('Enter a value: '))
# z = x+y
# print(z)

# ch = input('Enter a char: ').strip()[0]
# print(ch)

# x = eval(input('Enter an expr: ').strip())
# print(x)


import sys
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# print(x+y)

# u = int(input('Enter a number ').strip())
# u = eval(input('Enter an expr ').strip())
# print(int(input('Enter a num ').strip())**3)
# u = int(sys.argv[1])
# print(u**3) 

# from Practise_splvariable import *

# res = add(2,2)
# print(res)


# s=input().split(' ')
# l = [int(i) for i in input().split(' ')]
# print(s)

import math
import os
import random
import re
import sys



S = input()

try:
    print(int(S))
except:
    print('Bad String')