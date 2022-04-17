
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
            raise QueueFullException(Exception)
        else:
            self.rear = (self.rear + 1) % INITIAL_QUEUE_SIZE
            self.store[self.rear] = element
            self.size = self.size + 1

        return None
    


    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        return self.store.pop()

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        pass
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return len(self)

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return len(self.store) == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        return str(self.store)
