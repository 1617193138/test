Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/python
>>> list1 = ['physics', 'chemistry', 1997, 2000];
>>> list2 = [1, 2, 3, 4, 5, 6, 7 ];
>>> print "list1[0]: ", list1[0]
list1[0]:  physics
>>> print "list2[1:5]: ", list2[1:5]
list2[1:5]:  [2, 3, 4, 5]
>>> # -*- coding: UTF-8 -*-
>>> tup1 = (12, 34.56);
>>> tup2 = ('abc', 'xyz');
>>> # tup1[0] = 100;

>>> tup3 = tup1 + tup2;
>>> print tup3
(12, 34.56, 'abc', 'xyz')
>>> del tup1
>>> print tup1

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print tup1
NameError: name 'tup1' is not defined
>>> 
