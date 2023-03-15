# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:53:33 2023

@author: Murshid
"""
num = int(input("Enter no. of terms:"))

a=0
b=1

for i in range(num-2):
    c = a+b
    a=b
    b=c
print("The nth term is ",c)
