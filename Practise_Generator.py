# import time
# start_time = time.time()

# # Use generator when u want to fetch one value at a time and do processing instead of loading all value into memory at a time

# def topten():

#     n = 1

#     while n<=10:
#         sq = n*n
#         yield sq
#         n += 1

# val = topten() 
# # print(val.__next__())
# # print(val.__next__())
# # print(val.__next__())

# for i in range(1,11):
#     print(i//2)
# print("--- %s seconds ---" % (time.time() - start_time))

# for i in (val):
#     print(i//2)
# print("--- %s seconds ---" % (time.time() - start_time))
