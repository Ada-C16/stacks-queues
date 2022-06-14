
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
        if (self.front == 0 and self.rear == self.size -1) or (self.rear == (self.front-1)%(self.size-1)):
            raise QueueFullException
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
        elif (self.rear == self.size-1 and self.front != 0):
            self.rear = 0
            self.store[self.rear] = element
        else:
            self.rear += 1
            self.store[self.rear] = element

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.front == -1:
            raise QueueEmptyException

        element = self.store[self.front]
        self.store[self.front] = None

        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif (self.front == self.size-1):
            self.front = 0
        else:
            self.front += 1
        return element
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
        return self.size > 1

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        nonetype_removed = list(filter(None, self.store))
        return str(nonetype_removed)

