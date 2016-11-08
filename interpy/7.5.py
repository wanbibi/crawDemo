#!/usr/bin/env python
# encoding: utf-8

from random import randint
from functools import wraps
from functools import reduce
from collections import Counter


# def say(func):
#     @wraps(func)
#     def dosomething():
#         print 'before and fuck'
#
#         func()
#
#         print 'after and suck'
#     return dosomething
#
# @say
# def fuckoff():
#     print 'fuckofffffffffffffff'
#
#
#
# fuckoff()
#
# function = say(fuckoff)
# print function.__name__

def add(func):
    @wraps(func)
    def beforeAndAfter():
        print 'before'
        func()
        print 'after'
    return beforeAndAfter



@add
def say():
    print 'hello'

say()



def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run