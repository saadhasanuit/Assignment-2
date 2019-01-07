print("MUHAMMAD SAAD HASAN 18B-117-CS SECTION:-A")
print("ASSIGNMENT # 3")
print("EXERCISE 3.17")
## Use eval() function
## PART A
eval('2*3+1')
## PART B
eval('hello')#It will generate error which is because eval() function is used for integer and float
"""Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    eval('Hello')
  File "<string>", line 1, in <module>
NameError: name 'Hello' is not defined
"""
## PART C
eval("'Hello' + '' + 'World!'")
## PART D
eval("'ASCII'.count('I')")
## PART E
eval('x = 5')# It will generate error because eval function is not used for assigning string values
"""Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    eval('x = 5')
  File "<string>", line 1
    x = 5
      ^
SyntaxError: invalid syntax
"""
