# 894. Implement queue using Linkedlist


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedListQueue:
    def __init__(self):
        self.rear = None
        self.front = None

    def push(self, x):
        newNode = Node(x)
        if self.rear is None:
            self.rear = self.front = newNode
            return
        self.rear.next = newNode
        self.rear = newNode
 

    def pop(self):
        if self.isEmpty():
            return None
        if self.front == self.rear:
            v = self.front.data
            self.front = self.rear = None
            return v

        v = self.front.data
        self.front = self.front.next
        return v


    def peek(self):
        if self.isEmpty():
            return None
        return self.front.data
        
     

    def isEmpty(self):
        return self.front is None
