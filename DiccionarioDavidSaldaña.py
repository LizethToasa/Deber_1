Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> diccionario={'Liz':99847465, 'Kat':8494754848}
>>> diccionario['David']=94846756
>>> diccionario['Kat']
8494754848L
>>> diccionario
{'David': 94846756, 'Liz': 99847465, 'Kat': 8494754848L}
>>> diccionario['Andres']=746464646
>>> diccionario
{'Andres': 746464646, 'David': 94846756, 'Liz': 99847465, 'Kat': 8494754848L}
>>> list(diccionario.keys())
['Andres', 'David', 'Liz', 'Kat']
>>> sorted(diccionarios.keys())

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sorted(diccionarios.keys())
NameError: name 'diccionarios' is not defined
>>> sorted(diccionario.keys())
['Andres', 'David', 'Kat', 'Liz']
>>> 
