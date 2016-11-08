#!/usr/bin/env python
# encoding: utf-8

from random import randint
from functools import wraps
from functools import reduce
from collections import Counter
from collections import defaultdict
from collections import Counter
from collections import deque
from collections import namedtuple


colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

counter = Counter(k for k,v in colours)
print counter

d =deque()
d.append('1')
d.append('2')
d.append('3')

d.popleft()
x = deque(maxlen=10)

d.extendleft('0')
d.extend({5,4,3})
print d

print d

animal = namedtuple('animal','name age type')
me = animal(name='hi', age=31, type=2)
asdict = me._asdict()
print asdict
print me