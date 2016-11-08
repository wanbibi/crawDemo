#!/usr/bin/env python
# encoding: utf-8
from random import randint

i_ = [i for i in range(30) if i > 15]
print i_

range_ = [x * 2 for x in range(10)]
print range_

dict1 = {'2':'k'}

items_ = {v: k for k, v in dict1.items()}
print items_.keys()

in_ = {x * 2 for x in [2, 2, 2, 2]}
print in_
