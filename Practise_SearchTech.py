# Linear Search
# arr = [1,2,3,4,5,9]
# n = 9
# pos = -1
# def search(lst,n):
#     for i in range(len(lst)):
#         if lst[i] == n:
#             globals() ['pos'] = i
#             return True
#     return False

# if search(arr,n):
#     print('Found',n,'at position',pos)
# else:
#     print('Not Found',n)

# Binary Search
# pos = -1

# def binsearch(lst,n):
#     lower_bound = 0
#     upper_bound = len(lst)-1

#     while lower_bound <= upper_bound:
#         mid = (upper_bound + lower_bound)//2

#         if lst[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if lst[mid] < n:
#                 lower_bound = mid +1
#             else:
#                 upper_bound = mid -1

#     return False

# arr = [2,3,1,0,4,9]
# arr.sort()
# print(arr)
# n = 9

# if binsearch(arr,n):
#     print('Found',pos+1)
# else:
#     print('Not Found')

# Bubble Sort
# def sort(num):

#     for i in range(len(num)-1,0,-1):
#         for j in range(i):
#             if num[j] > num[j+1]:
#                 num[j],num[j+1] = num[j+1],num[j]



nums = [9,4,6,7,5,2]
# sort(nums)
# print(nums)

# Selection sort
# def sort(nums):
#     for i in range(len(nums)):
#         minpos = i
#         for j in range(i,len(nums)):
#             if nums[j] < nums[minpos]:
#                 minpos = j
#         temp = nums[i]
#         nums[i] = nums[minpos]
#         nums[minpos] = temp

#         print(nums)

# nums = [1,4,2,6,7,5]
# sort(nums)
# print(nums)

mini = 0
for i in range(len(nums)):
    if i == 0:
        mini = nums[i]
for j in range(len(nums)):
    if nums[j] < mini:
        temp = mini
        mini = nums[j]
        nums[j] = temp
print(mini)