from multiprocessing import Process
import multiprocessing
import os
import time

def hello():
    for i in "hello":
        print(i)
        time.sleep(1)

def word():
    for i in "word":
        print(i)
        time.sleep(1)

if __name__ == "__main__":

    process1 = multiprocessing.Process(target=hello)
    process1.start()
    process2 = multiprocessing.Process(target = word)
    process2.start()