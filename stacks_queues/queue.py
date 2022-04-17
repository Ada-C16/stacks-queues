
from tempfile import TemporaryFile


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

    def is_full(self):
        if self.size == self.buffer_size:
            self.store.insert(self.rear+1, None)
            self.buffer_size += 1
            self.front += 1

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        self.is_full()

        if self.front == -1:
            self.front = 0
            self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.buffer_size
        
        self.store[self.rear] = element
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException

        front = self.store[self.front]
        
        self.store[self.front] = None

        self.front = (self.front + 1) % self.buffer_size

        self.size -= 1

        return front
    
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
        if self.size == 0:
            return True
        return False


    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        queue = []

        index = self.front

        size = self.size

        while size > 0:
            queue.append(self.store[index])
            index = (index + 1) % self.buffer_size
            size -= 1

        return str(queue)