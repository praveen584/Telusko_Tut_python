from tempfile import tempdir


a = 4
b = 5
print(a,b)

# 1st
# a = a+b
# b = a-b
# a = a-b

# 2nd
# temp = a
# a = b
# b = temp

# 3rd
# a = a^b
# b = a^b
# a = a^b

# 4th
a,b = b,a # uses rot_two 
print(a,b)