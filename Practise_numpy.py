import numpy as np

# Creating array using numpy
# arr = np.array([1.1,2,3,4,5])
# print(arr)

# arr = np.linspace(1,15,10)
# print(arr)

# arr = np.arange(1,15,2)
# print(arr)

# arr = np.logspace(1,20,5)
# print("%.2f" %arr[1])

# arr = np.zeros(4)
# print(arr)

# arr = np.ones(4)
# print(arr)

# Array operation
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([1,2,3,4,5])
# print(arr1+arr2)
# print(np.sin(arr1))
# print(np.cos(arr1))
# print(np.log(arr1))
# print(np.sqrt(arr1))
# print(np.sum(arr1))
# print(np.min(arr1))
# print(np.max(arr1))
# print(np.sort(arr1))
# print(np.concatenate([arr1,arr2]))

# arr_c = arr1
# print(arr1)
# print(arr_c)
# print(id(arr1),id(arr_c))

# # Shallow copy when one array ele is changed other also changes
# arr_c = arr1.view()
# arr1[1] = 6
# print(arr1)
# print(arr_c)
# print(id(arr1),id(arr_c))

# # Deep copy when one array ele is changed other also changes
# arr_c = arr1.copy()
# arr1[1] = 4
# print(arr1)
# print(arr_c)
# print(id(arr1),id(arr_c))

# Adding array without using in built fun
# for i,j in zip(arr1,arr2):
#     print(i+j,end=' ')

# print()
# res = []
# for i in range(len(arr1)):
#     res.append(arr1[i]+arr2[i])
# print(res)

# Find max num from arr
# for i in range(len(arr1)):
#     if i==0:
#         max = arr1[i]
# for i in range(len(arr1)):
#     if arr1[i] > max:
#         max = arr1[i]
# print(max)

# Working with Matrix 
# arr = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)

# arr1 = arr.flatten()
# print(arr1)

# arr3 = arr1.reshape(2,2,3)
# print(arr3)

# m = np.matrix(arr)
# print(m)

# m1 = np.matrix('1 2 3; 4 5 6;7 8 9')
# m2 = np.matrix('1 2 3; 4 5 6;7 8 9')
# # print(m1)
# print(np.diagonal(m1))
# print(m1.min())
# print(m1.max())
# print(m1 * m2)

b = np.matrix(np.array([[1, 2, 3], [4, 5, 6]]))
a = np.matrix(np.array([[4, 5], [6, 2], [3, 9]]))
b1 = b.tolist()
a1 = a.tolist()

print(b.shape[0])
sum = 0
res = ''

for i in range(b.shape[0]):
    for j in range(b.shape[0]):
        sum = 0
        for k in range(b.shape[1]):
            sum += b1[i][k]*a1[k][j]
        res+=str(sum)+' '
    if i!= (b.shape[0]-1):
        res+=';'    
print(np.matrix(res))