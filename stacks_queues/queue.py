
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
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.front == -1:
            self.front = self.rear = 0

        if self.full():
            buffer_increase = int(self.buffer_size * 0.5)
            self.store = self.store[:self.rear] + [None] * buffer_increase + self.store[self.front:]
            self.buffer_size += buffer_increase
            self.front += buffer_increase

        self.store[self.rear] = element
        self.rear = (self.rear + 1)% self.buffer_size
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException("Queue is empty")
        element = self.store[self.front]
        self.front = (self.front + 1)% self.buffer_size
        self.size -= 1
        return element

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty():
            return None
        return self.store[self.front]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return self.size == 0

    def full(self):
        return self.size == self.buffer_size

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        values = []
        for i in range(self.front, self.front + self.size):
            pos = i % self.buffer_size
            values.append(self.store[pos])
        return str(values)
