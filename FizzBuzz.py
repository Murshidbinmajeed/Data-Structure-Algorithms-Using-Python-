# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:15:23 2023

@author: Murshid
"""

n=int(input("Enter a number :"))

for i in range(1,n+1):
    if i%3==0 and i%5==0:#checking if the number is both divisible by 3 and 5
        print("FizzBuzz")
    elif i%3==0:#checking if the number is  divisible by 3
        print("Fizz")
    elif i%5==0:#checking if the number is divisible by 5
        print("Buzz")
    else:
        print(i)
    
