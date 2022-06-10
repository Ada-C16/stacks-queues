
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
        # -1 is just a marker to indicate nothing in the list, we can mark as None as well
        self.size = 0
      

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.size == self.buffer_size:
            raise QueueFullException('Queue is full!')

        if self.size == 0:
            self.front = 0
            self.rear = 0
        self.store[self.rear] = element #insert where rear and front were pointing at first. But rear is the one moving to indicate the position of insert
        self.rear = (self.rear + 1) % self.buffer_size #the next insert position
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException
        front_element = self.store[self.front]
        self.store[self.front] = None
        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1
        return front_element
        # check if empty, if so raise an exception
        # find and store the front element
        # move front to the next index
        # return the old front elements
        # front and rear are indexes, like 0, 1

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
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
        return self.front == self.rear

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        queue_list = []
        start_index = self.front
        while (start_index % INITIAL_QUEUE_SIZE) < INITIAL_QUEUE_SIZE and len(queue_list) < self.size:
            if self.store[start_index % INITIAL_QUEUE_SIZE] is not None:
                queue_list.append(self.store[start_index % INITIAL_QUEUE_SIZE])
                start_index += 1
            else:
                start_index += 1
        return str(queue_list)


