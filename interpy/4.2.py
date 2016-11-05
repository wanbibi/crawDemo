#!/usr/bin/env python
# encoding: utf-8
from random import randint

numberList =  xrange(-5,10)
moreThanZero = filter(lambda x: x > 0, numberList)
zhengshu = filter(lambda x: x % 3 == 0, numberList)
print zhengshu
print moreThanZero
