from gevent import monkey; monkey.patch_socket()
import urllib2

req = urllib2.Request('http://www.google.com')
response = urllib2.urlopen(req)
page = response.read()

print(page)


'''
In this example ,
urllib2 lib is performing IO intensive task. As gevent doesn't implement
interface for urllib , But as it has implementation of premetive lib like
socket . We could orderride implementation of socket interface used in urlib2

This is possible by importing monkey.patch_socket() method.

'''
