#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:20:19 2023

@author: ayaanali
"""

def encrypt(string, shift): 
 
  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
 
text = input("Enter message: ")
s = int(input("Enter shift value: "))
print("Encrypted Text: ", encrypt(text, s))

