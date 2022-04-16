
# from threading import Thread
# from time import sleep


# class Hello(Thread):

#     def run(self):
#         for i in range(10):
#             print('Hello')
#             sleep(1)

# class Hi(Thread):

#     def run(self):
#         for i in range(10):
#             print('Hi')
#             sleep(1)

# h1 = Hello()
# h2 = Hi()

# h1.start()
# sleep(0.2)
# h2.start()

# h1.join()
# h2.join()

# print('Bye')

# Using multithreading, exceptional handling
from threading import Thread
from time import sleep
import sys
from typing import final

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    print('Factorial of {} is {}'.format(n,f))

def square(n):
    print('Square of {} is {}'.format(n,n*n))

if __name__ == '__main__':

    n = input('Enter a num for number of times taking input or quit q/Q: ').strip()
    ct = 1
    try:
        if n=='q' or n=='Q':
            print('Quitting')
            sys.exit(1)
        else:
            while ct<=int(n):
                try:
                    inpt = int(input('Enter a num to get factorial: ').strip())
                    try:
                        t1 = Thread(target=factorial,args=(inpt,))
                        t2 = Thread(target=square,args=(inpt,))
                        t1.start()
                        sleep(0.2)
                        t2.start()

                        t1.join()
                        t2.join()
                    except Exception as e:
                        print('Something went wrong',e)
                    finally:
                        print('Completed',ct,'times')
                except ValueError as e:
                    print('Invalid Input')
                ct += 1
    except ValueError as e:
        print('Invalid Input')
    finally:
        print('End')