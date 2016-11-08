#!/usr/bin/env python
# encoding: utf-8
from random import randint

def add(value,value2):
    global result
    result = value+value2


add(2,4)
print result

def profile():
    name = 'danny'
    age = 30
    return name,age


fuck = profile()
print fuck[1]

