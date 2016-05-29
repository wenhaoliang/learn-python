import time
import multiprocessing

def hello():
    for i in "hello":
        print(i)
        time.sleep(1)

def world():
    for i in "world":
        print(i)
        time.sleep(2)

if __name__ == "__main__":
    for i in range(2):
        pr = multiprocessing.Process(target=hello)
        pr.start()
        print(i)
    # for i in range(2):
    #     pr = multiprocessing.Process(target=world)
    #     pr.start()
    # for i in range(4):
    #     pr.join()
    #
    # print("Over")
