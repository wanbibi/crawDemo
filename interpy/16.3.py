#!/usr/bin/env python
# encoding: utf-8
from random import randint
from pprint import pprint
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key = lambda x:x[1])
print a
