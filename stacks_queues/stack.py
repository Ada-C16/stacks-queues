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
        self.store.add_first(element)

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        if self.store.head is None:
            raise StackEmptyException
        
        current = self.store.head
        pop_val = self.store.head.value
        if current.next:
            self.store.head = current.next
            self.store.head.previous = None
        else:
            self.store.head = self.store.tail = None
        
        return pop_val

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        if self.store.head is None:
            return True
        return False

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        result = []

        if self.store.head is None:
            return str(result)

        current = self.store.head
        while current:
            result.append(current.value)
            current = current.next

        return str(result)
