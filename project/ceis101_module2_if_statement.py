# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 06:18:59 2024

CEIS110 Module 2 "Selection Control Structures"

The IF satement

"""

name = input('What is your name: ')
city = input('What city do you live in: ')
temperature = float(input('What is the temperature: '))
if temperature > 60:
    # The commands following the IF statement will be indented by a tab
    # That is, every command that is indented will be exectuted
    # when the IF test is TRUE
    print('Hello ', name, 'from', city, 'it is nice where your live.')
    print('Cheers')
else:
    # But if the IF test is FALSE, then the commands under the ELSE
    # will be excuted. That is, all the commands that are indented 
    # by a tab following the ELSE statement will be executed when
    # the IF test is FALSE
    print('Hello ', name,'from', city, 'it is cold where your live.')
    print('Bye')