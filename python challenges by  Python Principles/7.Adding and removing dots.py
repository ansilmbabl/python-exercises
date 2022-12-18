"""
Adding and removing dots
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""

#my solution................................
def add_dots(s):
    x=""
    for i in s:
        x += i + "." 
    x=x[:len(x)-1]
    return x
    
def remove_dots(s):
    x=""
    for i in s:
        if i!=".":
            x+=i
    return x
    
s="test"
print(remove_dots(add_dots(s)))

...........................................



................................................
#solution
# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")
  
..............................................
