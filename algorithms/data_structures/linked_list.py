"""
    Singly Linked List
    ------------------
    A linked list is a data structure consisting of a group of nodes which
    together represent a sequence. Under the simplest form, each node is
    composed of data and a reference (in other words, a link) to the next
    node in the sequence; more complex variants add additional links. This
    structure allows for efficient insertion or removal of elements from any
    position in the sequence.

    Pseudo Code: https://en.wikipedia.org/wiki/Linked_list
"""

class ListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList(object):
    """Base object for all types of linked list object"""
    def append(self, data):
        raise NotImplemented

    def search(self, data):
        raise NotImplemented

    def remove(self, data):
        raise NotImplemented

    @property
    def size(self):
        return self._size

class SinglyLinkedList(LinkedList):

    def __init__(self, *args):
        self._size = 0
        self.head = None
        for arg in args:
            self.append(arg)

    def append(self, data):
        """Inserting a node in linked list O(N)"""
        if not self.head:
            self.head = ListNode(data)
            self._size = 1
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = ListNode(data)
            node.next = new_node
            self._size += 1

    def append_front(self, data):
        """Inserting can be done on O(1) if it is done front"""
        node = ListNode(data)
        node.next = self.head
        self._size += 1
        self.head = node

    def __contains__(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def remove(self, data):
        node = self.head
        prev_node= None
        while node:
            if node.data == data:
                prev_node.next = node.next
                self._size -= 1
                return True
            prev_node = node
            node = node.next
        return False

class DoublyLinkedList(LinkedList):

    def __init__(self, *args):
        self._size = 0
        self.head = None
        for arg in args:
            self.append(arg)

    def append(self, data):

        if not self.head:
            self.head = ListNode(data)
            self._size = 1
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = ListNode(data)
            node.next = new_node
            new_node.prev = node
            self._size += 1

    def append_front(self, data):

        node = ListNode(data)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self._size += 1 

    def __contains__(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def remove(self, data):
        node = self.head
        prev_node = None
        next_node = None
        while node:
            next_node = node.next
            if node.data == data:
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                self._size -= 1
                return True
            prev_node = node
            node = node.next
        return False

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
