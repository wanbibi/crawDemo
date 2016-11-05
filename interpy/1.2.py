#!/usr/bin/env python
# encoding: utf-8

def x(**args):
    for key,value in args.items():
        print key,value


print x(name = 'asdf', age = 16)
