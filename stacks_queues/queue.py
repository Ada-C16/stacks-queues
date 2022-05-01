
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

        if (self.front == (self.rear + 1)%(len(self.store))):
            raise QueueFullException("Queue is full!")
        elif self.front == -1:  # Queue is empty
            self.front = 0
            self.rear = 0
            self.store[0] = element
            self.size += 1
            return str(self)
        else: 
            self.rear = (self.rear + 1) % len(self.store)
            self.store[self.rear] = element
            self.size += 1
            return str(self)
        

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.front == -1:
            QueueEmptyException("The queue is empty!!!")
            return None

        start = self.store[self.front]
        if self.rear == self.front:
            self.rear = -1
            self.front = - 1
        elif self.front == len(self.store) - 1:
            self.front = 0
        else:
            self.front += 1
        self.size -= 1

        return start

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
        return True if self.size == 0 else False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        if self.front == -1:
            return "[]"
        else:
            return_string = "["
            i = self.front
            for x in range(self.size):
                if x + 1 == self.size: # This would be the last value
                    return_string = return_string + str(self.store[i]) + "]"
                else:
                    return_string = return_string + str(self.store[i]) + ", "
                    if i < len(self.store) - 1:
                        i += 1
                    else:
                        i = 0    
        return return_string



