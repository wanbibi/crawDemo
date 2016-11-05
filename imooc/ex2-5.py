#!/usr/bin/env python
# encoding: utf-8
# 快速查找公共键
from random import randint, sample

goal = sample('abcdefg', randint(3, 5))
s1 = {x: randint(1, 4) for x in goal}
s2 = {x: randint(1, 4) for x in goal}
s3 = {x: randint(1, 4) for x in goal}
s4 = {x: randint(1, 4) for x in goal}
res = []
for k in s1:
    if k in s2 and k in s3 and k in s4:
        res.append(k)
print res

viewkeys1 = s1.viewkeys()
print viewkeys1
viewkeys2 = s2.viewkeys()
viewkeys3 = s3.viewkeys()
viewkeys4 = s4.viewkeys()
map_ = map(dict.viewkeys(), [viewkeys1, viewkeys2, viewkeys3, viewkeys4])
print map_

reduce(lambda a, b: a & b, map_)
