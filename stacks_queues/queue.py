
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE   # -> [, , , , ]
        self.buffer_size = INITIAL_QUEUE_SIZE # -> int, 
        self.front = -1
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.size >= self.buffer_size:
            raise QueueFullException
        else:   # 8/23 
            if self.rear != len(self.store) - 1:
                if self.size == 0:
                    self.front += 1
                self.store[self.rear+1] = element
                self.rear += 1
                self.size += 1
            else: 
                self.rear = 0
                self.store[self.rear] = element
                self.size += 1
        

        
            

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.size == 0:
            raise QueueEmptyException
        else:
            pop = self.store[self.front]
            if self.size == 1:
                self.rear -= 1
            self.store[self.front] = None
            self.front += 1
            self.size -= 1
            return pop
        

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.front == -1:
            return None
        else:
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
        res_str  = '[' 
        if self.rear >= self.front:
            res_str  = '['  
            for i in range(self.front, self.rear):
                res_str += str(self.store[i]) + ", "
        else:
            for i in range(self.front, len(self.store)):
                res_str += str(self.store[i]) + ", "
            for i in range(0, self.rear):
                res_str += str(self.store[i]) + ", "
        res_str += str(self.store[self.rear]) + "]"            
        return res_str
        
            
        
