import heapq

class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0
    def append(self,ele, priority):
        heapq.heappush(self._queue,(-priority, self._index,ele))
        self._index +=1
    def pop(self):
        return heapq.heappop(self._queue)[-1]


pq = PriorityQueue()
pq.append('a',3)
pq.append('bob',1)
pq.append('john',4)
print(pq.pop())
print(pq.pop())

