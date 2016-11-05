#!/usr/bin/env python
# encoding: utf-8
from random import randint
from functools import reduce

reduce1 = reduce((lambda x, y: x + y), [2, 2, 5, 6])
print reduce1


def add(x, y):
    return x * y


reduce2 = reduce(add, [4, 5, 6])
print reduce2
