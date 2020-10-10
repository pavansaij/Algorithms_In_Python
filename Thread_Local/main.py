import threading
from Paginated import Paginated
from NonPaginated import NonPaginated
from WebPost import Sample

threads = []
s = Sample()
p1 = Paginated()
p2 = NonPaginated()

for index in range(5):
    x = threading.Thread(target=p1.per, args=(s,))
    threads.append(x)

for index in range(5,10):
    x = threading.Thread(target=p2.per, args=(s,))
    threads.append(x)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
