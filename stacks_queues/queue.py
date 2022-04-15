
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
        if self.empty():
            self.front = 0
            self.rear = 0
        elif self.rear == self.front:
            raise QueueFullException("Queue is full!")
        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException("Queue is empty!")
        else:
            result = self.store[self.front]
        self.front = (self.front + 1) % self.buffer_size
        if self.front == self.rear:
            self.front = -1
        return result

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty():
            return None
        else:
            return self.store[self.front]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        if self.empty():
            return 0
        else:
            size = (self.buffer_size - (self.front - self.rear)) % self.buffer_size
            return self.buffer_size if size == 0 else size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return self.front == -1

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        if self.empty():
            return str([])
        if self.front < self.rear:
            return str(self.store[self.front:self.rear])
        else:
            result = []
            first_half = self.store[self.front:]
            second_half = self.store[:self.rear]
            return str(first_half + second_half)
