#!/usr/bin/env python
# encoding: utf-8
from random import randint
from functools import reduce
from collections import Counter


def hi():
    return 'hi'

def beforeSayHi(func):
    print 'what did you say ?'
    print func
beforeSayHi(hi())

