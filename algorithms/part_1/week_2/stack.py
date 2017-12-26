# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:04:36 2017

@author: User
"""

class LinkedStack:
    class Node:
        def __init__(self):
            self.item = None
            self.next = None
    
    def __init__(self):
        self.first = None
    
    def isEmpty(self):
        return self.first == None
    
    def push(self, item):
        old_first = self.first
        self.first = self.Node()
        self.first.item = item
        self.first.next = old_first
        
    def pop(self):
        item = self.first.item
        self.first = self.first.next
        return item
    
stack = LinkedStack()
stack.push('A')
stack.push('B')
print(stack.pop())
stack.push('C')
print(stack.pop())
print(stack.pop())