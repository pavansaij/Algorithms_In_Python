import threading


def synchronized(lock=None):
    if lock is None:
        lock = threading.Lock()

    def synced_func(func):
        def wrapped(*args, **kws):
            with lock:
                return func(*args, **kws)
        return wrapped

    return synced_func