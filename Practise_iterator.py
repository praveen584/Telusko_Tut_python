n = [1,2,33,4]
# print(n[3])

# for i in range(len(n)):
#     print(n[i],end=' ')

# it = iter(n)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# class TopTen():

#     def __init__(self):
#         self.num= 1

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.num <= 10:

#             val = self.num
#             self.num += 1

#             return val
#         else:
#             raise StopIteration

# values = TopTen()

# for i in values:
#     print(i)