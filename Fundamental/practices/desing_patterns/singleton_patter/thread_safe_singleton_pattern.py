import threading


class ThreadSafeThread:
    _instance = {}

    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


singleton = ThreadSafeThread()
print(singleton.__hash__())

singleton = ThreadSafeThread()
print(singleton.__hash__())
