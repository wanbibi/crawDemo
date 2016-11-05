#!/usr/bin/env python
# encoding: utf-8
from random import randint
from functools import reduce
from collections import Counter

def hi(name='helo'):
    return 'hi'+name

print hi()

greert = hi

print (greert())

del hi
print hi()

print greert()

