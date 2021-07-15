# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:06:21 2021

@author: Enrique Velasco
"""

class Stack:
    
    class _Node:
        
        def __init__(self, value):
            self.value = value
            self.next_node = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        
        array = []
        current_node = self.head
        
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next_node
        
        return str(array) + " Size: " + str(self.size)
    
    def push(self, value):
        
        new_node = self._Node(value)
        
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        
        self.size += 1
        
            
            
    def pop(self):
        
        if self.size > 1:
            new_head = self.head.next_node
            self.head.next_node = None
            self.head = new_head
            
            self.size -= 1
        else:
            self.head = None
            self.tail = None
            
            self.size = 0

stack = Stack()

stack.push('A')
stack.push('B')
stack.push('C')
stack.push('D')
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

            