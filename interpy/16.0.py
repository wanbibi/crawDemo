#!/usr/bin/env python
# encoding: utf-8
from random import randint

try:
    file = open('d:\\fuck.txt', 'a')
except IOError as ioe:
    print 'error is happened'
finally:
    print 'fuck'