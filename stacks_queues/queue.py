
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
        # Handles the rear_ptr
        if self.front == -1:
            self.front = 0
            self.rear = 1
            self.store[self.front] = element
            self.size += 1
            return self.store

        elif self.size == self.buffer_size:
            raise QueueFullException

        else:
            self.store[self.rear] = element
            self.rear = (self.rear + 1) % self.buffer_size
            self.size += 1
            return self.store
            
        
        

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        #Handles the head_ptr
        if self.front == -1:
            raise QueueEmptyException

        data = self.store[self.front]
        self.size -= 1
        self.store[self.front] = None
        self.front = (self.front + 1) % self.buffer_size

        if self.size == 0:
            self.front = -1
            self.rear = -1

        return data



    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.front == -1:
            return None
        
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
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        q = []
        for i in range(self.size):
            q.append(self.store[(self.front + i) % self.buffer_size])
        
        return str(q)
