import threading

lock = threading.Lock()

with lock:
    print('Critical section 1')
    print('Critical section 2')
