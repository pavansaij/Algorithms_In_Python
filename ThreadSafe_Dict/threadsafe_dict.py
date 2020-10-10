from collections.abc import MutableMapping
import threading

class ThreadLocalDict(MutableMapping):
    __thread_local = threading.local()

    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)
        ThreadLocalDict.__thread_local.__setattr__("store", self.__dict__)

    def __setitem__(self, key, value):
        try:
            ThreadLocalDict.__thread_local.__getattribute__("store")[key] = value
        except:
            ThreadLocalDict.__thread_local.__setattr__("store", {key:value})

    def __getitem__(self, key):
        return ThreadLocalDict.__thread_local.__getattribute__("store")[key]

    def __delitem__(self, key):
        del ThreadLocalDict.__thread_local.__getattribute__("store")[key]

    def __iter__(self):
        return iter(ThreadLocalDict.__thread_local.__getattribute__("store"))

    def __len__(self):
        try:
            return len(ThreadLocalDict.__thread_local.__getattribute__("store"))
        except:
            return 0
    
    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except:
            return False

    def clear(self):
        ThreadLocalDict.__thread_local.__delattr__("store")


    def __str__(self):
        return str(ThreadLocalDict.__thread_local.__getattribute__("store"))
    def __repr__(self):
        return r'{}, MutableDict({})'.format(super(ThreadLocalDict, self).__repr__(), 
                                  ThreadLocalDict.__thread_local.__getattribute__("store"))