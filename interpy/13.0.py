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

list2 = ['apple','banana','orange','pear']
for k,v in enumerate(list2 ,3):
    print k,v
list1 = list(enumerate(list2, 1))
print list1
