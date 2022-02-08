# https://towardsdatascience.com/python-linked-lists-c3622205da81


class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
    
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        return '->'.join([str(node) for node in self])

    def __len__(self):
        cnt = 0
        node = self.head
        while node:
            cnt+=1
            node = node.next
        return cnt

    @property
    def values(self):
        return [node.value for node in self]

    def add_multiple_nodes(self, values):
        for v in values:
            self.add_node(v)

    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail