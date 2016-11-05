#!/usr/bin/env python
# encoding: utf-8

items = [2,4,5,6,7]
res = []
for i in items:
    res.append(i*i)
print res
list1 = list(map(lambda x:x**x,items))
print list1


def jia(x):
    return x+1

def jian(x):
    return x-1

funcs = [jia,jian]
for i in range(1,5):
    print i
    value = map(lambda x:x+10, items)
    print(list(value))