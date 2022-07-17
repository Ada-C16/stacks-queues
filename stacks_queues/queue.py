
from asyncio import QueueFull


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
        if self.size == INITIAL_QUEUE_SIZE:
            raise QueueFullException()
        if self.size == 0:
            self.front = 0
            self.rear = 0
            self.size = 1
            self.store[self.front] = element
            return
        
        if self.rear == INITIAL_QUEUE_SIZE - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.size += 1
        self.store[self.rear] = element

        

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.size == 0:
            raise QueueEmptyException()
        to_ret = self.store[self.front]
        self.store[self.front] = None
        if self.front == INITIAL_QUEUE_SIZE - 1:
            self.front = 0
        else:
            self.front += 1
        self.size -= 1

        return to_ret

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.size == 0:
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

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        to_print = []
        i = self.front
        for _ in range(self.size):
            to_print.append(self.store[i])
            if i == INITIAL_QUEUE_SIZE - 1:
                i = 0
            else:
                i += 1
        return str(to_print)