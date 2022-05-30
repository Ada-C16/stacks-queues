from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
        """

        self.store.add_last(element)
        # if not self.store.head:
        #     self.store.add_first(element)
        #     return
        # self.store.tail.next = element
        # self.store.tail = element

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if not self.store.head:
            raise StackEmptyException
            
        value = self.store.tail.value
        if self.store.head == self.store.tail:
            self.store.head = self.store.tail = None
        else:
            self.store.tail.next = None
            self.store.tail = self.store.tail.previous
        
        return value
            
            
        


    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if not self.store.head:
            return True
        return False


    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        values = []

        current = self.store.tail
        while current:
            values.append(str(current.value))
            current = current.previous

        return ", ".join(values)
