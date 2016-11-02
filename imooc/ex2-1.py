#筛选数据
from random import randint

data = [randint(-10, 10) for _ in xrange(20)]
print data

l = filter(lambda x: x >= 0, data)

x_ = [x for x in data if x >= 0]

print x_

d = {x: randint(60, 100) for x in xrange(1, 21)}
print d

v_ = {k for k in d.iterkeys() if k > 10}
print v_

s = set(data)

if_x_ = {x for x in s if x % 3 == 0}
print if_x_
