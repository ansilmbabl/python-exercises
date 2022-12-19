"""
Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
"""
#my solution.................
def format_number(s):
    n=""
    while s > 999:
        x=(s%1000)
        if x==0:
            n=",00"+str(x)+n
        else:
            n=","+str(x)+n
        s=s//1000
    n=str(s)+n
    return n
    
.............................

#solution.................................
# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)
