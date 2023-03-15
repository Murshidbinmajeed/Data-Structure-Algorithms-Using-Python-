# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:24:44 2023

@author: Murshid
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)
        self.count += 1
    
    def _insert(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        elif val > node.val:
            if not node.right:
                node.right = Node(val)
            else:
                self._insert(node.right, val)
    
    def delete(self, val):
        if not self.root:
            return
        else:
            self._delete(self.root, val)
        self.count -= 1
    
    def _delete(self, node, val):
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                min_val = self._find_min(node.right)
                node.val = min_val
                node.right = self._delete(node.right, min_val)
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.val
    
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)
    
    def size(self):
        return self.count

bst=BST()
while True:
    print("Click the appropriate option::1.Insert  2.Delete 3.Search  4.Size  5.To quit ::")
    n=int(input())
    if n==1:
        print("Enter the element to be inserted:")
        item = int(input())
        bst.insert(item)
        print("\n")
    elif n==2:
        value=int(input("Enter the value to be deleted:"))
        result=bst.delete(value)
        print("The deleted Item is ",result)
        print("\n")
    elif n==3:
        print("Enter the element to be searched:")
        value=int(input())
        result=bst.search(value)
        if result==True:
            print("The value is found in the tree")
        else:
            print("The value NOT found in the tree")
        print("\n")
    elif n==4:
        size=bst.size()
        print("The size of the tree is ",size)
        print("\n")
        
    elif n==5:
        break
    else:
        print("Enter the correct option")
        print("\n")
