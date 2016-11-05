#!/usr/bin/env python
# encoding: utf-8
from random import randint
from functools import reduce
from collections import Counter


def hi(name='hi2'):
    def greet():
        return 'ff'

    def welcome():
        return 'bb'

    if name == 'hi':
        return greet
    else:
        return welcome


fuckoff = hi()
print fuckoff
