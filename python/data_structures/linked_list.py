class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.val = Node(value)
        self.val.next = self.head
        self.head = self.val

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
        current = current.next
        return False

    def __str__(self):
        current = self.head
        string = ""
        while current is not None:
            string += "{ " + str(current.value) + " } -> "
            current = current.next
        return string + "NULL"

    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def insert_before(self, before, value):
        current = self.head
        previous = None
        try:
            while current.value is not before:
                previous = current
                current = current.next
            if previous is not None:
                previous.next = Node(value, current)
            if previous is None:
                self.head = Node(value, current)
        except Exception as e:
            raise TargetError(e)

    def insert_after(self, after, value):
        current = self.head
        try:
            while current.value is not after:
                current = current.next
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
        except Exception as e:
            raise TargetError(e)


class TargetError:
    pass
