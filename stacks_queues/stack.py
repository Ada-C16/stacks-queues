from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        # self.store = LinkedList()
        self.store = list()

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
        """
        self.store.append(element)
        

        

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
    
        if len(self.store) == 0:
            raise StackEmptyException
        else:
            return self.store.pop()
        

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if len(self.store) == 0:
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        string_stack = self.store[::-1]
        return str(string_stack)
