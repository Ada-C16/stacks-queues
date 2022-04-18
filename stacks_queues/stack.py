from xml.dom.minidom import Element
from stacks_queues.linked_list import LinkedList, Node

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
        """

        self.store.add_first(element)

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if self.store == None:
            raise StackEmptyException("The stack is already empty!")
        temp = self.store.get_first()
        self.store.remove_first()
        return temp

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if self.store.get_first == None:
            return True
        return False

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        my_string = '[' + self.store.visit() + ']'
        return my_string
