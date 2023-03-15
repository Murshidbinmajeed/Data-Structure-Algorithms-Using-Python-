# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:53:29 2023

@author: Murshid
"""
def countSort(arr):

    output = [0 for i in range(len(arr))]
 
    count = [0 for i in range(256)]

    result = ["" for i in arr]

    for i in arr:
        count[ord(i)] += 1
 
    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        result[i] = output[i]
    return result

str1=input("Enter the first string:")
str2=input("Enter the second string:")

s1=countSort(str1)
s2=countSort(str2)

if s1==s2:
    print("True")
else:
    print("False")
