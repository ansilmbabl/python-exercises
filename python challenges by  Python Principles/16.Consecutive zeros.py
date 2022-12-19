"""
Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""

#my solution...............................
def consecutive_zeros(s):
    c=0
    maxm=0
    l=[]
    for i in s:
        if i == "0":
            c+=1
            maxm=c
            l.append(maxm)
        else:
            l.append(maxm)
            c=0
    return max(l)
  
.........................................

#solution................................................
# naive solution
def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
  
..........................................................
