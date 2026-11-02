# 919. Implement stack using Linkedlist

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.isEmpty():
            return None
        v = self.head.data
        self.head = self.head.next
        return v

    def top(self):
        if self.isEmpty():
            return None
        return self.head.data
     

    def isEmpty(self):
        return self.head is None
