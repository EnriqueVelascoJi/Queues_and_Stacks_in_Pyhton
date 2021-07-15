# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:30:31 2021

@author: Enrique Velasco
"""

#QUEUE
#Structure FIFO

class Queue:
    
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
    
    def enqueue(self, value):
        
        new_node = self._Node(value)
        
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        
        self.size += 1
        
    def dequeue(self):
        
        current_node = self.head
        counter = 0
        
        if self.size - 2 >= 0:
            while counter != self.size - 2:
                current_node = current_node.next_node
                counter += 1
                
            current_node.next_node = None
            
            self.size -= 1
        else:
            self.head = None
            self.tail = None
            self.size = 0
        
        
        
queue = Queue()

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')
print(queue)

queue.dequeue()
print(queue)

queue.dequeue()
print(queue)

queue.dequeue()
print(queue)

queue.dequeue()
print(queue)

queue.dequeue()
print(queue)
            