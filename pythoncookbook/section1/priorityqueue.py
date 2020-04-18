import heapq

class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0
    def append(self,ele, priority):
        heapq.heappush(self._queue,(ele,priority, self._index))
        self._index +=1
    def pop(self):
        return heapq.heappop(self._queue)


pq = PriorityQueue()
pq.append('a',3)
print(pq.pop())

