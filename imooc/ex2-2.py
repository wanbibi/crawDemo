# coding=utf-8
# 为元素命名
# utf
from collections import namedtuple

NAME, AGE, SEX, EMAIL = xrange(4)
student = ('jim', 20, 'male', 'hh@qq.com')
print student[SEX]
student2 = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = student2('2', 2, 'male', 'sdfas@qq.com')
print s

print s.name

print isinstance(s,tuple)
