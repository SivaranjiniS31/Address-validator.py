Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def addressVal(address):
...     dot = address.find(".")
...     at = address.find("@")
...     if (dot == -1):
...         print("Invalid")
...     elif (at == -1):
...         print("Invalid")
...     else:
...         print("Valid")
... 
... print("This program will decide if your input is a valid email address")
... while(True):
...     print("A valid email address needs an '@' symbol and a '.'")
...     x = input("Input your email address:")
... 
