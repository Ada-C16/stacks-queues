
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
        """ Adds an element to the Queue.
            Raises a QueueFullException if all elements
            in the store are occupied.
            Returns None.
        """
        if self.size == self.buffer_size:
            raise QueueFullException("Queue is full!")

        if self.size == 0: 
            self.front = self.rear = 0

        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty(): 
            raise QueueEmptyException("Queue is empty.")

        removed_element = self.store[self.front]
        self.store[self.front] = None
        self.front += 1
        self.size -= 1

        return removed_element

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty(): 
            return None

        return self.store[self.front]

    def get_size(self):
        """ Returns the number of elements in
            the Queue
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
        values = []

        if self.front < self.rear: 
            for index in range(self.front, self.rear): 
                values.append(self.store[index])
        
        else: 
            for index in range(self.front, self.buffer_size):
                values.append(self.store[index])
            for index in range(0, self.rear):
                values.append(self.store[index])

        return str(values)


