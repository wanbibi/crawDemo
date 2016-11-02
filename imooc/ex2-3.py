# coding=utf-8
#统计单词出现频度
from random import randint
from collections import Counter
import re


data = [randint(-10, 10) for _ in xrange(20)]
print data
c2 = Counter(data)
print c2
common = c2.most_common(1)
print common


txt = open('C:\\Users\\Administrator\\Desktop\\a.txt').read()
re_split = re.split('\W+', txt)
counter3 = Counter(re_split)
print counter3

most_common = counter3.most_common(3)
print most_common
