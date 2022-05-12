from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
       self.store.add_last(element)

    def pop(self):
        if self.store.length == 0:
            raise StackEmptyException
        else:
            return self.store.remove_last()

    def empty(self):
        return self.store.length() == 0

    def __str__(self):
        result = []
        for i in range(self.store.length):
            result.append(self.store.get_first())
            self.store.remove_first()

        return result
