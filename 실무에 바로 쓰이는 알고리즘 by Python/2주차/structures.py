# 연결 리스트
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

# 스택
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.val

    def is_empty(self):
        return self.top is None
    
# 큐
class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.val

    def is_empty(self):
        return self.front is None