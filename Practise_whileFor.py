# c = 1

# while c <= 5:
#     print('While loop ',end="",sep=' ')
#     c1 = 1
#     while c1 <= 4:
#         print('Inside ',end="",sep=' ')
#         c1 += 1
    
#     c += 1
#     print()

# n = 1
# while n <= 100:
#     if n % 3 == 0 or n % 5 == 0:
#         print(f'Skipping the num {n}') 
#     else:
#         print(n)
#     n += 1

# n = 1
# while n <= 4:
#     print('*'*5)
#     n += 1

# x = [1,2,3,4]

# for i in x:
#     print(i,end=' ')
# print()
# for i in [4,5,'g',6]:
#     print(i,end='')

# for i in range(2,10,2):
#     print(i)

# for i in range(20,10,-2):
#     print(i)

# for i in range(1,50):
#     if i**2 <= 50:
#         print(i**2)
#     else:
#         break

# n = int(input('Enter a num: '))
# ct = 1
# av = 5

# while ct < n:
#     if ct > av:
#         break
#     print('Eat Chocolate')
#     ct += 1

# for i in range(1,11):
#     if i%3==0 or i%5==0:
#         continue
    
#     print(i)
    
# while ct <= n:
#     if ct%2!=0:
#         pass
#     else:
#         print(ct)
#     ct += 1

# fibonacci
# a=0
# b=1
# n = 10
# l = []
# for i in range(n):
#     if i==0:
#         l.append(b)
#         print(b,end=" ")
#     elif i==1:
#         l.append(b)
#         print(b,end=" ")
#     elif i > 1:
#         sum = l[i-1]+l[i-2]
#         l.append(sum)
#         print(sum,end=" ")


# n = int(input('Enter a num: '))
# a,b = 0,1
# ct = 0

# if n <= 0:
#     print('Wrong inpt ')
# elif n == 1:
#     print(b,end=" ")
# else:
#     while ct < n:
#         print(a,end=" ")
#         s = a + b
#         a = b
#         b = s
#         ct += 1

# prime
# n = int(input('Enter a num '))

# for i in range(1,n):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 print('Composite num',i)
#                 break
#         else:
#             print('Prime num',i)

# n = int(input('Enter a range: '))
# sum = 0
# for i in range(2,n):
#     if i%2==0 and i!=2:
#         continue
#     else:
#         print(i)
#         sum += i
# print(sum)

# Pattern
# for j in range(4):
#     print('# '*4)

# for i in range(4):
#     for j in range(4):
#         print('# ',end="")
#     print()

# for i in range(4):
#     print('# '*(i+1))

# for i in range(4):
#     for j in range(i+1):
#         print('# ',end='')
    
#     print()

# for i in range(4,0,-1):
#     for j in range(i):
#         print('# ',end="")
#     print()

# for i in range(4):
#     for j in range(i+1,5):
#         print(j,end='')
#     print()

# s = 'ABCD'
# s1 = 'PQR'

# for i in range(4):
#     print(s[:i+1]+s1[i:])

# l = [11,22,51,54,23]
# for i in range(0,len(l)):
#     if l[i]%5==0:
#         print(l[i])
#         break
# else:
#     print('End')

n = 3

for i in range(2,n):
    if n%i==0:
        print('Composite num',n)
        break
else:
    print('Prime num',n)