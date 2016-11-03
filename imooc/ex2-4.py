#!/usr/bin/env python
# encoding: utf-8
from random import randint

sorted1 = sorted([2, 76, 2, 4, 76, 7, 3, 4, 5])
print sorted1

b = {x: randint(60, 100) for x in 'xydkegs'}

print b

sorted2 = sorted(b)
print sorted2

keys = b.keys()
print keys

zip_ = zip(b.itervalues(), b.iterkeys())
print zip_

score = sorted(zip_)
print score

items = b.items()
print items

sorted3 = sorted(b.items(), key=lambda x: x[1])
print sorted3
