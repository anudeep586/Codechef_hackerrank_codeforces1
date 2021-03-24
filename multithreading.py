import time
import threading
def print_86(numbers):
    for i in numbers:
        time.sleep(0.2)
        print("86",i)
def print_(numbers):
    for j in numbers:
        time.sleep(0.5)
        print("print",j)
numbers=[2,3,4,5]
t1=threading.Thread(target=print_86,args=(numbers,))
t2=threading.Thread(target=print_,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
