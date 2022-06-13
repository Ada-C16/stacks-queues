
from logging import raiseExceptions
from tracemalloc import start


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
            self.front = 0
            self.rear = 0
        elif self.size == self.buffer_size:
            raise QueueFullException('Queue is full')
        

        self.store[self.rear] = element
        self.rear = (self.rear + 1)% self.buffer_size
        self.size += 1 

    
    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.

        """

        #Check if Queue is empty and if so raise Exception
        # Get the element from the front 
        # Front will go to the next index in list 
        # Change size 
        # Check if the list is empty 

        # deque takes element off the queue, and return the element (Min's comment)
        
        if self.size ==0:
            raise QueueFullException('Queue is empty')

        #in order to deque, you must set self.front to self.front + 1% self.buffer_size
        deque = self.store[self.front] 
        self.front = (self.front +1) % self.buffer_size
        self.size -= 1 
        return(deque)

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.store[self.front]:
            return self.front
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
        else: 
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        
        element_list = []
        start_position = self.front
        # next starts at zero therefore it cannot be used as the index on line 125 because FIFO method deques front position and shift to the next index 
        for next in range (self.size):
            # is element not being used? Says it is not accessed but need it to loop through range 
            element_list.append(self.store[start_position])
            start_position = (start_position + 1) % self.buffer_size
        return str(element_list)
        
        
            

        

        
