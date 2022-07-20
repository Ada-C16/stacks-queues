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
        self.stack_size += 1 
        self.stack_list.append(element)

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if self.is_empty():
            return None 
        self.stack_size -=1 
        return self.stack_list.pop()

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        return self.stack_size() == 0
        
    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        pass
