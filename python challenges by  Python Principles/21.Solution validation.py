"""
Solution validation
The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
"""
 
#my solution.....................................................
def validate(s):
    if "def" not in s:
        return "missing def"
    if ":" not in s:
        return "missing :"
    if "(" and ")" not in s:
        return "missing paren"
    if "()"+":" in s:
        return "missing param"
    if "    " not in s:
        return "missing indent"
    if "validate" not in s:
        return "wrong name"
    if "return" not in s:
        return "missing return"
    return True
  
................................................................

#aolution.................................................
def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True
...........................................................
