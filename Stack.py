# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 21:33:27 2023

@author: Murshid
"""
#Python code to implement stack

stack=[]

def push(item):
    stack.append(item)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        element=stack[-1]
        del stack[-1]
        print("The popped element is ",element)
        print(stack)

def peek():
    element = stack[-1]
    return element

def is_empty():
    if not stack:
        print("The stack is empty")
    else:
        print("The stack is not empty")
    
while True:
    print("Click the appropriate option::1.Push 2.Pop 3.peek 4.is_empty 5.To quit :")
    n=int(input())
    if n==1:
        print("Enter the element to push:")
        item = int(input())
        push(item)
    elif n==2:
        pop()
    elif n==3:
        item=peek()
        print("The element on top is ",item)
        
    elif n==4:
        is_empty()
    elif n==5:
        break
    else:
        print("Enter the correct option")
        
    
    
