from sqlalchemy import true
from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
            stacks -> last in first out 
        """
        self.store.add_last(element)
        return element
    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if not self.store:
            raise StackEmptyException("List is empty")

        return self.store.remove_last()  
        # tests fails when it returns None
        

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        return self.store.empty()

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next

        return ", ".join(values)


stack = Stack()
stack.push(10)
stack.pop()