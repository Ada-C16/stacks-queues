
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
            raise QueueFullException("Queue is full!")

        if self.size == 0:
            self.front = 0
            self.rear = 0

        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException("Queue is empty!")
    
        front_ele = self.store[self.front]
        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1
        return front_ele


    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if not self.store:
            return None
        return self.store[0]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.store.size

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
        str_list_form = []
        start = self.front

        for i in range(self.size):
            str_list_form.append(self.store[start])
            start = (start + 1) % self.buffer_size
        return str(str_list_form)
