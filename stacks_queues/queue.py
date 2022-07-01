
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        self.buffer_size = INITIAL_QUEUE_SIZE
        self.front = -1
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        if len(self.store) == self.size:
            raise QueueFullException("QUEUE IS FULL")
        
        self.store[self.rear] = element
        self.size += 1
        self.rear = (self.rear+1)% self.buffer_size
        

    def dequeue(self):
        if self.size == 0:
            raise QueueEmptyException("QUEUE IS EMPTY")
        
        element = self.store[self.front]
        self.size -= 1
        self.store[self.front] = None
        self.front = (self.front +1) % self.buffer_size
        return element

    def front(self):
        if self.size > 0:
            return self.store[self.front]

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def __str__(self):
        q = []
        start = self.front
        while len(q) < self.size:
            q.append(self.store[start])
            if start < len(self.store) - 1:
                start += 1
            else:
                start = 0
        return str(q)
