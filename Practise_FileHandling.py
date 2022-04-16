import os
path = os.getcwd()

f = open(path+'/Telusko/FileHandling/test.txt','r') # reading file

# print(f.read())
# print(f.readline(),end='')
# print(f.readline())

# f2 = open(path+'/Telusko/FileHandling/abc.txt','a') # append mode to append with current data into file
# f2.write(' Laptop')

# f1 = open(path+'/Telusko/FileHandling/abc.txt','w') # writing file

# for data in f:
#     f1.write(data)

f = open(path+'/Telusko/FileHandling/HDwallpaper.jpg','rb')

f1 = open(path+'/Telusko/FileHandling/NewHDwallpaper.jpg','wb')

for i in f:
    f1.write(i)