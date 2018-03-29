Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ass¡á = set[(asshole,erection,impotent)]
SyntaxError: invalid syntax
>>> ass = set[(asshole,erection,impotent)]

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ass = set[(asshole,erection,impotent)]
NameError: name 'asshole' is not defined
>>> ass = set([asshole,erection,impotent])

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ass = set([asshole,erection,impotent])
NameError: name 'asshole' is not defined
>>> ass = set(['asshole','erection','impotent'])
>>> 
