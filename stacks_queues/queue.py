
INITIAL_QUEUE_CAPACITY = 20


class QueueFullException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_CAPACITY
        self.buffer_size = INITIAL_QUEUE_CAPACITY
        self.front = -1
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        # not a valid index
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.size == self.buffer_size:
            raise QueueFullException("Queue is full")

        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.size == 0:
            raise QueueEmptyException("Queue is empty")

        # Grab the item we want to remove
        item = self.store[self.front]
        # replace the value in the array with None so we don't hold memory longer than we need to
        self.store[self.front] = None

        # Update state variables
        self.size -= 1
        self.front = (self.front + 1) % self.buffer_size

        # If we just removed the last item from the queue, set the front and rear to -1,
        # representing an empty state (see constructor)
        if self.size == 0:
            self.front = -1
            self.rear = -1

        return item

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.size == 0:
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
        return self.size == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        if self.size == 0:
            return "[]"

        list = []

        loop_end = (self.rear) if (
            self.rear > self.front) else len(self.store)
        for item in range(self.front, loop_end):
            list.append(str(self.store[item]))

        if self.rear <= self.front:
            for item in range(0, self.rear):
                list.append(str(self.store[item]))

        return "[" + ", ".join(list) + "]"
