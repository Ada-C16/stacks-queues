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
      
    def isFull(self):
          if ((self.front == 0 and self.rear == self.buffer_size - 1) or
      (self.rear == (self.front-1)%(self.buffer_size-1))):
              return True
          else:
              return False

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.isFull():
            raise QueueFullException("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.store[self.rear] = element
            self.size += 1
        elif (self.rear == len(self.store) - 1 and self.front!=0):#if need to wrap
            self.rear = 0
            self.store[self.rear] = element
            self.size += 1
        else:
            self.rear += 1
            self.store[self.rear] = element
            self.size += 1
        return None

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if (self.front == -1): # Queue is empty
            raise QueueEmptyException("Queue is empty")
        
        data = self.store[self.front]
        #overwrite the element being deleted
        self.store[self.front] = None

        #if there was only one element in the queue
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
            self.size = 0
        elif (self.front == self.buffer_size-1): # if front needs to wrap around
            self.front = 0
        else:
            self.front += 1

        self.size -= 1
        return data


    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if not self.empty():
            return self.store[self.front]
        else: 
            return None
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return True if self.front == -1 else False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        temp = []
        for i in range(self.size):
            index = (self.front + i)%self.buffer_size
            temp.append(self.store[index])
        return temp[:].__str__()










      
#     # def isFull(self):
#     #     return ((self.front == 0 and self.rear == self.size-1) or self.front == self.rear + 1)
     

#     def enqueue(self, element):
#         """ Adds an element to the Queue
#             Raises a QueueFullException if all elements
#             In the store are occupied
#             returns None
#         """
#         if self.front == -1:
#             self.front = self.rear = 0
#             self.store[self.rear] = element
#             self.size += 1
#         elif self.rear == len(self.store) - 1:
#             self.rear = 0
#             self.store[self.rear] = element
#             self.size += 1
#         else:
#             self.rear += 1
#             self.store[self.rear] = element
#             self.size += 1
#         return None
  
            

#     def dequeue(self):
#         """ Removes and returns an element from the Queue
#             Raises a QueueEmptyException if 
#             The Queue is empty.
#         """
#         if self.store.length() == 0:
#             raise QueueFullException("Queue is empty")
#             return None
#         else:
#             self.size -= 1
#             self.front = self.store.get_first().next
#             return self.store.remove_first()

