import gevent
from gevent import socket

'''
Implementation 1
'''
urls = ["www.google.com","www.agrostar.in","www.facebook.com"]
jobs = [gevent.spawn(socket.gethostbyname,url) for url in urls ]
gevent.joinall(jobs,timeout=2)
print([job.value for job in jobs])


'''
Instead we could also write code as below
Implementation 2
'''

import socket
urls = ["www.google.com","www.agrostar.in","www.facebook.com"]
print([socket.gethostbyname(url) for url in urls])


'''
Difference between implementations:
In first implementation gevent has its own socket lib implementation which works
asynchronously.
When we call spawn(), it calls method gethostbyname(), and switches its execution for
calling next gethostbyname() method, and so in a asynchronous way.

In the second method, we call synchronously .

'''
