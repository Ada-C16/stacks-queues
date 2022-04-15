
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
        if self.size == self.buffer_size:
            raise QueueFullException('Queue is full')

        if self.size == 0:
            self.front = 0
            self.rear = 0
        
        self.store[self.rear] = element
        print(self.store[self.rear])
        print(self.store)
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1



    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        #check if empty, raise exception
        #find and store the front *element* in a temp variable
        #move front to the next index
        #return old front element

        if self.size == 0:
            raise QueueEmptyException('Queue is empty')

        temp = self.store[self.front]
        self.store[self.front] = None
        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1

        return temp



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
        if self.size == 0:
            return True

    def __str__(self):

        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        int_list = self.store[:]
        int_list = list(filter(None, int_list))
        string_list = [str(int) for int in int_list]
        my_string = ', '.join(string_list)
        result = '[' + my_string + ']'
        return result

        # new_list = self.store[:]
        # new_list = list(filter(None, new_list))
        # #new_list[:None] == new_list[:]

        # # for i in range(len(new_list)):
        # #     if new_list[i] == None:
        # #         new_list.pop(i)
        
        # string_list = ', '.join(new_list)
        # result = '[' + string_list + ']'
        # print(result)
        # return result
        

        # for i in range(self.size):
        #     my_list.append(self.store[(self.front + i) % self.buffer_size])
        #     return my_list


