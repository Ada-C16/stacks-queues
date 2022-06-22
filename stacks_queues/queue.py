
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
        
        if self.front == (self.rear+1 % self.buffer_size):
            # Re: (self.front == 0 and self.rear == self.size -1) 
            # Should be checking self.rear against BUFFER_SIZE, not self.size. Otherwise, this expression will always return True even though the Queue still has spaces left. 
            # Note that self.front is not always at index 0.
            # Re: modulo operator
            # self.rear + 1 is the same as self.rear +1 % buffer_size in any case except for where rear is the last index of the list (where self.rear = 19), need to go back to 0 (wrap around to the front)
            raise QueueFullException
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
        elif (self.rear == self.buffer_size-1 and self.front != 0):
            self.rear = 0
            self.store[self.rear] = element
        else:
            self.rear += 1
            self.store[self.rear] = element
        
        self.size += 1


    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        element_to_be_dequeued = self.store[self.front]
        self.store[self.front] = None

        if self.front == -1:
            raise QueueEmptyException

        elif self.front == self.rear:
            self.front = -1
            self.rear = -1

        elif self.front == self.buffer_size-1:
            self.front = 0
            self.rear -= 1
        else:
            self.front += 1

        self.size -= 1

        return element_to_be_dequeued

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
        return self.size == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
    
        nonetype_removed = list(filter(None, self.store))

        nonetype_removed.sort()
        return str(nonetype_removed)