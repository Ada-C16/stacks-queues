
from re import T
from xml.dom.minidom import Element


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
        if self.buffer_size == self.size:
            raise QueueFullException
        if (self.rear + 1) == self.buffer_size:
            self.rear = 0
            self.size += 1
            self.store[self.rear] = element
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
            raise QueueEmptyException
        if (self.front + 1) == self.buffer_size:
            self.front = 0
            self.size -= 1
            return self.store[self.front]
        else:
            self.front += 1
            self.size -= 1
            return self.store[self.front]


    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.size == 0:
            return None
        else:
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
        else:
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        index = self.front
        lst = []
        for _ in range(self.size):
            lst.append(self.store[(index +1) % self.buffer_size])
            index += 1
        return str(lst)

