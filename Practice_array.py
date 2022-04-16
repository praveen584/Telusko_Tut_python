import array as ar

from numpy import array

# from numpy import array

vals = ar.array('i',[1,2,3,-3,4])
# print(vals,type(vals))
# print(vals.buffer_info())
# vals.reverse()
# print(vals,vals.typecode)

# for i in range(len(vals)):
#     print(vals[i])

new_ar = ar.array(vals.typecode,(a*a for a in vals))
# for i in new_ar:
#     print(i)

# i = 0
# while i < len(new_ar):
#     print(new_ar[i])
#     i += 1

# from array import *
# valori = array('i',[109,10000,1009082,4,8,7,3,4,2])
# while True:
#     print(sorted(valori))
#     break

# arr = ar.array('i',[])

# l = int(input('Enter the len of array: '))

# for i in range(l):
#     x = int(input('Enter the val in array: '))
#     arr.append(x)

# print(arr)

# n = int(input('Enter a num to be checked: ').strip())

# idx = 0
# for i in arr:
#     if i == n:
#         print(idx)
#         break
#     idx += 1

# print(arr.index(n))

# 1) Create an array with 5 values & delete the value at index no. 2 without using in-built function. 
# 2) write a code to reverse an array without using in-built function.

arry = ar.array('i',[])
n = int(input('Enter a len of array: '))

for i in range(n):
    x = int(input('Enter a num of array: '))
    arry.append(x)

print(arry)

val = int(input('Enter an index to be deleted: '))

for i in range(len(arry)):
    if i == val:
        arry = arry[:val]+arry[val+1:]
print(arry)

n_l = []
for i in range(len(arry),0,-1):
    n_l.append(i)
print(n_l)