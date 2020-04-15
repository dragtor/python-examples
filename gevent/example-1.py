import gevent 
from gevent import socket

urls = ["www.google.com","www.agrostar.in","www.facebook.com"]
jobs = [gevent.spawn(socket.gethostbyname,url) for url in urls ]
gevent.joinall(jobs,timeout=2)
print([job.value for job in jobs])


''' 
Instead we could also write code as below 
'''

import socket
urls = ["www.google.com","www.agrostar.in","www.facebook.com"]
print([socket.gethostbyname(url) for url in urls])


'''
Difference between implementation: 
In first implementation gevent has its own socket lib implementation which works 
asynchronously .
when we call spawn it calls method  gethostbyname , and switch it execution for
calling next gethostbyname method , and so on in asynchronuse way. 

In second methods , we call methods synchronouly .

'''

