# Using a circular buffer with an internal array starting at 20 elements, implement a Queue with the following methods:

# - `enqueue(value)` - Adds the value to the back of the queue.
#   - This method should raise a `QueueFullException` if the buffer size is exceeded (20 elements).
# - `dequeue` - removes and returns a value from the front of the queue
# - `empty?` returns true if the queue is empty and false otherwise
# Fist in first out

from pytest import Item


INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        self.buffer_size = INITIAL_QUEUE_SIZE
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.size == self.buffer_size:
            raise QueueFullException('This will break it')
        
        # the last element 
        self.rear = (self.rear +1) % self.buffer_size
        self.store[self.rear] = element
        self.size = self.size +1


    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        #  find element in the store
        # First in first out 
        if self.size == 0:
            raise QueueEmptyException('This will break it')
        else:
            val = self.store[self.front]
            self.front = self.front + 1 % self.buffer_size
        
        # decrease size
        self.size = self.size - 1
        return val

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.store[self.front]:
            return self.store[0]
        else:
            return None    

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
        values = []
        index = self.front
    
        for i in range(self.size):
            values.append(self.store[index])
            index = (index + 1) % self.buffer_size
        return str(values)