import threading
import time

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting" + self.name)
        print_time(self.name,self.threadId,self.counter)
        print("Exiting" + self.name)

def print_time(thread_name,delay,counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s %s" % (thread_name,time.ctime(time.time())))
        counter -= 1

thread1 = myThread(1,"thread1",5)
thread2 = myThread(2,"thread2",5)

thread1.start()
thread2.start()