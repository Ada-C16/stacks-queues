
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
        if self.empty():
            self.front = 0
            self.rear = 0
        elif self.rear == self.front:
            raise QueueFullException("Queue is full!")
        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            raise QueueEmptyException
        else:
            removed = self.store[self.front]    
            self.store[self.front] = None
            self.front = (self.front + 1) % self.buffer_size
            if self.front == self.rear:
                self.front = self.rear = -1
        self.size -= 1
        return removed

    def front(self):
        if self.empty():
            return None
        else:
            return self.store[self.front]
        

    def size(self):
        if self.empty():
            return 0
        else:
            return self.size

    def empty(self):
        return self.front == -1

    def __str__(self):
        if self.empty():
            return str([])
        if self.front < self.rear:
            return str(self.store[self.front:self.rear])
        else:
            result = []
            first_half = self.store[self.front:]
            second_half = self.store[:self.rear]
            return str(first_half + second_half)
