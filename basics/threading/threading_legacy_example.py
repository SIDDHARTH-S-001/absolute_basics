import _thread
import time

def thread_delay(thread_name, delay):
    counter = 0
    print("debug line")
    while counter < 3:
        time.sleep(delay)
        counter = counter + 1
        print(f"Thread {thread_name} -----> {time.time()}")

_thread.start_new_thread(thread_delay, ("t1", 1)) # 'start_new_thread' created 'daemon' like threads with no wway to 'join'.
_thread.start_new_thread(thread_delay, ("t2", 3))

time.sleep(10) # Keep main thread alive until these 2 threads finish.