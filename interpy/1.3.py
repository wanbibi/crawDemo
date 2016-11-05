#!/usr/bin/env python
# encoding: utf-8

def test_args_kwargs(arg11, arg2, arg3):
    print("arg1:", arg11)
    print("arg2:", arg2)
    print("arg3:", arg3)

def test_args(*args):
    for arg in args:
        print arg

k={"arg11":'arg2','arg2':234,'arg3':66}
print test_args_kwargs(**k)

def another_function(arg,*args):
    print "single",arg
    for arg in args:
        print 'not single',arg

print another_function('hello',4,5,6)