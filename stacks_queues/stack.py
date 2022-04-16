from logging import raiseExceptions
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
        return None

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if not self.store:
            raise StackEmptyException
        return self.store.remove_last()

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if self.store.empty():
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        return str(self.store)
