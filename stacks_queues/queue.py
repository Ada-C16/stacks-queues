
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
        # check if full
        if self.size == self.buffer_size:
            raise QueueFullException('Queue is full!')

        # check if empty
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
        # check if empty, raise exception
        if self.size == self.buffer_size:
            raise QueueEmptyException('Queue is empty!')
        
        # find and store front element
        temp = self.front

        # move front to next index
        self.front = (self.front + 1)
        self.size -= 1
        
        # return old front element
        return temp

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
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
        return self.size == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        result = []
        if self.size == 0:
            return result
        elif self.rear >= self.front:
            self.queue

        # while self.front != None:
        #     element = self.dequeue()
        #     result.append(element)
        # return str(result)

# queue = Queue()
# queue.enqueue(10)
# print(queue)