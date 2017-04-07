import threading

lock = threading.Lock()

lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    lock.release()
