"""
Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""

#my solution.................. 
def mid(s):
    m=""
    if len(s)%2 != 0:
        m = s[len(s)//2]
        return m
    else:
        return m

s1="abc"
s2="aaaa"
print(mid(s1))
print(mid(s2))


#output
"b"
""
.............................


................................................................
# solution
# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]
