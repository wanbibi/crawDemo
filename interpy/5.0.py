#!/usr/bin/env python
# encoding: utf-8
from random import randint
from functools import reduce
from collections import Counter

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print duplicates

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
fuckoff = set(['red', 'fuck'])
print fuckoff.intersection(valid)

valid1 = set(['yellow', 'red', 'blue', 'green', 'black'])
fuckoff2 = set(['red', 'fuck'])
print fuckoff2.difference(valid)

a_ = {'a'}
print  type(a_)
