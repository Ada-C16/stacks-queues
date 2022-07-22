from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:
    #This stack implementation overloads the LinkedList underneath it
    #to make life easy.  In true software dev fashion, no need to 
    #reinvent the wheel.

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
        """
        return self.store.add_first(element)
        

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if self.store.length == 0:
            raise StackEmptyException ("stack is empty")

        return self.store.remove_first()

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        self.store.length = 0
        if self.store.length == 0:
            return True
        return False

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        return self.store.__str__

