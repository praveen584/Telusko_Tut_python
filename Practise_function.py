# def greet():
#     print('Hello')
#     print('Good morning')

# greet()

# def add(a,b):
#     return a+b,a-b

# res1,res2 = add(2,2)
# print(res1,res2)

# def update(x):
#     print(id(x))
#     x[1] = 8
#     print(id(x))
#     print("x ",x)

# a = [1,2,3]
# print(id(a))
# update(a)
# print("a ",a)

# def add(a,*b):
#     res = a
#     for i in b:
#         res += i
#     print(res)

# def person(name,age=18):
#     print(name)
#     print(age)

# person(name="1",age=20) #keyword arg
# person(name="1",age=27) #default arg
# add(1,2,3,4) # variable length or * wildcard multiple values

# def person_det(**kwargs):
#     for i,j in kwargs.items():
#         print(i,':',j)

# person_det(name='Tejas',age=27,role='Datascientist') #keyword variable length

# a = 4
# def something():
#     a = 5
#     x = globals()['a']
#     print('In fun',a)
#     globals()['a'] = 8

# something() # Preference will be given to local variable
# print('Out fun',a)

# def count(lst):
#     even = odd = 0

#     for i in range(len(lst)):
#         if lst[i]%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd

# lst = [1,2,3,4,5,3,66,3,2,44,9]
# e,o = count(lst)
# print("Even : {} and Odd : {}".format(e,o))


from functools import reduce
from numpy import get_array_wrap


# lst = [input(f'Enter a {i} name: ').strip() for i in range(int(input('Enter no of name: ').strip()))]

# def count(lst):
    
#     great = 0
#     lower = 0

#     for i in range(len(lst)):
#         if len(lst[i]) > 5:
#             great += 1
#         else:
#             lower += 1

#     return great,lower

# great,lower = count(lst)
# print(great,lower)

# Fibonacci series
# def fib(n):
#     a=0
#     b=1
#     if n <= 0:
#         print('Wrong input',n)
#     elif n==1:
#         print(a,end=" ")
#     else:
#         print(a,end=" ")
#         print(b,end=" ")
#         for i in range(2,n):
#             c = a+b
#             if c < 100:
#                 a = b
#                 b = c
#                 print(c,end=" ")
            

# n = int(input('Enter a num to get fibonacci series less than num: ').strip())
# fib(n)

# Factorial
# n = int(input('Enter a num to get factorial: ').strip())

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f = f*i

#     return f

# import sys
# print(sys.getrecursionlimit())
# def fact(n):
#     f=1
#     for i in range(n,0,-1):
#         f *= i

#     return f

# res = fact(n)
# print(res)

# Recursion
# def fact(n):
#     if n==0:
#         return 1

#     return n*fact(n-1)

# res = fact(n)
# print(res)


# def square(n):
#     return n*n

# f = lambda a:a*a
# res = f(5)
# print(res)

# f = lambda a,b:a+b
# res = f(5,5)
# print(res)

# n = [1,2,3,2,3,5,4,7,8,5,8,9]

# def is_even(n):
#     return n%2==0

# even = list(filter(is_even,n))
# even = list(filter(lambda n:n%2==0,n)) # filter with lambda
# even_doubles = list(map(lambda a:a+2,even)) # map with lambda
# sum = reduce(lambda a,b:a+b,even_doubles) # reduce with lambda

# a = {1,2,3,4,4,5}
# sum_s = reduce(lambda a,b:a+b,a)
# print(sum_s)

# print(even)
# print(even_doubles)
# print(sum)

# Decorator

def div(a,b):
    print(a/b)

def smart_div(func):
    def check(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return check

d = smart_div(div)
d(3,6)