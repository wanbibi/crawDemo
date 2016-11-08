#!/usr/bin/env python
# encoding: utf-8

from functools import wraps
import requests


def logging(func):
    @wraps(func)
    def printlogin(*args, **kwargs):
        print (func.__name__+" was called.")
        return func(*args, **kwargs)
    return printlogin

@logging
def add(x):
    return x*x


i = add(4)
