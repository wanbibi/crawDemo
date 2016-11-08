#!/usr/bin/env python
# encoding: utf-8
from random import randint
from pprint import pprint

my_dict = {'name': 'hi', 'age': 20}
pprint(my_dict)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
