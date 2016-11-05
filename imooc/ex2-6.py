#!/usr/bin/env python
# encoding: utf-8
# 让字典保持有序
from collections import OrderedDict
from random import randint
from time import time

ordered_dict = OrderedDict()
plays = list('ABCDEFG')
start = time()

for i in xrange(plays.__len__()):
    raw_input()
    pop = plays.pop(randint(0, plays.__len__() - 1))
    end = time()
    ordered_dict[pop] = (i + 1, end - start)

for k in ordered_dict:
    print k, ordered_dict[k]
