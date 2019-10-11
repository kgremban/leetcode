class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        pointer = self.head
        count = 0
        while pointer:
            count += 1
            pointer = pointer.get_next()
        return count

    def search(self, data):
        pointer = self.head
        while pointer:
            if pointer.get_data() == data:
                return pointer
            else:
                pointer = pointer.get_next()

        if pointer is None:
            raise ValueError("Data not in list")

    def delete(self, data):
        pointer = self.head
        previous = None
        while pointer:
            if pointer.get_data() == data:
                if previous is None:
                    self.head = pointer.get_next()
                else:
                    previous.set_next(pointer.get_next())
            else: 
                previous = pointer
                pointer = pointer.get_next()
        if pointer is None:
            raise ValueError("Data not in list")