
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
        if self.size == self.buffer_size:
            raise QueueFullException('Queue is full!')

        # if queue is empty
        if self.size == 0:
            self.front = 0
            self.rear = 0
        self.store[self.rear] = element
        # reassigns rear usng mod
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1       

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        # check if empty, if so raise an exception
        # Find and store the front element
        # move front to the next index
        if self.empty():
            raise QueueEmptyException('Queue is empty!')

        # store front element to return
        front = self.store[self.front]
        # remove by making it none
        self.store[self.front] = None
        #reassigns front
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
        return self.front
        

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
        current = self.front
        
        while len(values) < self.size:
            if self.store[current % self.buffer_size]:
                values.append(self.store[current % self.buffer_size])
                current += 1
        return str(values)
  