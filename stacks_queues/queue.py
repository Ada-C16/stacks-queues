
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
            raise QueueFullException ("Queue is full")

        if self.size == 0:
            self.front = 0
            self.rear = 0

        #per the test, don't duplicate the item if it was just enqueued
        if self.store[(self.rear - 1 ) % self.buffer_size] != element:
            self.store[self.rear] = element
            self.rear = (self.rear + 1 ) % self.buffer_size
            self.size = self.size + 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        #Check if empty, if so raise an exception
        if self.size == 0:
            raise QueueEmptyException("Queue is empty")

        retVal = self.store[self.front]
        #Find and store the front element
        self.store[self.front] = None
        #Move front to the next index
        self.front = (self.front + 1 ) % self.buffer_size
        # self.rear = (self.rear + 1 ) % self.buffer_size
        self.size = self.size - 1    
        return retVal    

        

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
        returnArr = []

        #if the queue rolls around past the buffer
        #we will break it into two loops        
        if self.front + self.size > self.buffer_size:
            for i in range (self.front, (self.size - (self.buffer_size % self.size))): 
            # keeping this hear in case we dont want to do the modulo math above and
            # really want to iterate through to the self.buffer_size as the end of the range
            # if self.store[i] != None:
                returnArr.append(self.store[i])

            for i in range (0, self.front): 
                if self.store[i] != None:
                    returnArr.append(self.store[i])   
        else:
            for i in range (0, self.rear + 1): 
                if self.store[i] != None:
                    returnArr.append(self.store[i])   

        returnString = '[' + ', '.join(str(x) for x in returnArr) + ']'

        return returnString
