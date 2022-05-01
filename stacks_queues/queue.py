
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
        if self.store.length() == self.buffer_size:
            raise QueueFullException("Queue is full")
            return None
        else:
            self.store.add_last(element)
            self.size += 1
            self.rear += 1
            return None

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.store.length() == 0:
            raise QueueFullException("Queue is empty")
            return None
        else:
            self.size -= 1
            self.front += 1
            return self.store.remove_first()

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
        pass

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        pass

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        pass
