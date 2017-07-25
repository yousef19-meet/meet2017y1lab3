Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = "bananayellowthinkhatgreyBIGcalifornia314"
>>> my_string= [12:17]
SyntaxError: invalid syntax
>>> my_string = [12:17]
SyntaxError: invalid syntax
>>> my_string[12:17]
'think'
>>> my_string[12:17]+my_string[24:27]
'thinkBIG'
>>> my_string[12:17]+print(" ")+my_string[24:27]
 
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    my_string[12:17]+print(" ")+my_string[24:27]
TypeError: Can't convert 'NoneType' object to str implicitly
>>> my_string[12:17]+my_string[24:27]
'thinkBIG'

>>> meet_value= my_string[12:17]+my_string[24:27]
>>> meet_value
'thinkBIG'
>>> 
