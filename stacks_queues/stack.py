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
        if self.store.head == None:
            return None
        return self.store.remove_last()
        # return None

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        return self.store.empty

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        if self.empty:
            return "[]"
        else:
            values = []
            current = self.store.head
            while current.next:
                values.append(str(current.value))
                current = current.next
            da_string = ", ".join(values)
            return "[" + da_string  + "]"