import time
from collections import deque

def search(lines , pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line , previous_lines 
        previous_lines.append(line)

def iterate_log(fp ):
    while True:
        line = fp.readline()
        if not line:
            continue
        yield line

'''
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line , prevlines in search(f, '3', 5):
            print(prevlines)
            print(line,end=' bagh')
            print('-'*20)
'''

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for l in iterate_log(f):
            print(l.strip())
    
