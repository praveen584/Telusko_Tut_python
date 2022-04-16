# Compile time error - like syntax error
# Logical error - Due to wrong logic Wrong output is thrown
# Runtime error - occur becoz of wrong input or code taking to long time to execute

a= 6
b = 3
try:
    print('Open')
    print(a/b)
    n = int(input('Enter a num: '))
except ZeroDivisionError as e:
    print('Do not divide by zero',e)
except ValueError as e:
    print('Invalid Input')
except Exception as e:
    print('Something went wrong',e)
finally:
    print('Closed')

print('Bye')