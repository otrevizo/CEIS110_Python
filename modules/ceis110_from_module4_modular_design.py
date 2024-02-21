# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:50:58 2024

CEIS110 Module 4 Lesson in Canvas

Functions
"""
#this function will display a message. The message is passed to the function as an argument
def print_welcome(message):
    print(message)
    print()
    
def main():
    message="Yeah baby!!"
    print_welcome(message)
    
#The following code checks whether the current module is the main module
if __name__ =="__main__":
    main();
    
    