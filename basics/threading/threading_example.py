import threading
import time

def thread_delay(thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(f"Thread {thread_name} -----> {time.time()}")

def cube_volume(a):
    print(f"Volume of cube = {a*a*a}")

class ThreadClass(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.delay = delay

    def run(self):
        print("Starting thread: ", self.name)
        thread_delay(self.name, self.delay)
        print("Execution of Thread: ", self.name, "is complete!")

###### Example 1: Basic Example
# t1 = threading.Thread(target=thread_delay, args=("t1", 1))
# t2 = threading.Thread(target=thread_delay, args=("t2", 3))

# t1.start() # 'start' method starts the thread & must be called 'at most' once for a thread.
# t2.start() # 'start' method will raise RUNTIMEERROR if called multiple times.

# input("Press Enter to interrupt threads")
# print("Threads interrupted, but they'll continue until they finish")

# t1.join() # blocks main thread until the thread t1 is finished if timeout=None. Can set a timeout as well.
# t2.join() 
# print("This will execute only after t1 completes")

###### Example 2: args as an interable
# t1 = threading.Thread(target=cube_volume, args=(2)) # will raise an error, as args must be a interable (list / tuple) not a single value.
# t1 = threading.Thread(target=cube_volume, args=(2, )) # add a "," to make it a tuple. This will work.
# t1.start()
# t1.join()
# print("Process complete")

###### Example 3: Threading as a sub-class.
t1 = ThreadClass("t1", 1)
t2 = ThreadClass("t2", 3)
t1.start()
t2.start()
t1.join()
t2.join()
print("Execution Complete")


