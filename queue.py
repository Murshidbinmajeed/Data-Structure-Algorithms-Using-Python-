# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:35:18 2023

@author: Murshid
"""
queue=[]

def enqueue(item):
    queue.append(item)
    print(queue)
    
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        item = queue[0]
        del queue[0]
        print("The deleted item is : ",item)
        print(queue)

def peek():
    item = queue[0]
    print("The item at front is ",item)

def is_empty():
    if not queue:
        print("The queue is empty ")
    else:
        print("The queue is not empty ")

while True:
    print("Click the appropriate option::1.enqueue 2.dequeue 3.peek 4.is_empty 5.To quit :")
    n=int(input())
    if n==1:
        print("Enter the element to push:")
        item = int(input())
        enqueue(item)
    elif n==2:
        dequeue()
    elif n==3:
        item=peek()
        print("The element on top is ",item)
        
    elif n==4:
        is_empty()
    elif n==5:
        break
    else:
        print("Enter the correct option")
    
    
