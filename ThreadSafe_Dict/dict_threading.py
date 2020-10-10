from threading import Thread
from threadsafe_dict import ThreadLocalDict
import threading
from synchronized import synchronized

shared_dict = ThreadLocalDict()

lock = threading.Lock()

def use_dict():
    for key, value in shared_dict.items():
        print(threading.get_ident(), " : ", key, " : ", value)

def process_dict(from_t):
    global shared_dict

    for i in range(2):
        shared_dict[(i,threading.get_ident())] = i+1
    
    use_dict()

    shared_dict.clear()

for i in range(4):
    Thread(target=process_dict, args=(i,)).start()