"""
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""

#my solution..................................
def is_anagram(x,y):
    dx={}
    dy={}
    
    for i in x:
        if i not in dx:
            dx[i]=1
        else:
            dx[i]+=1
        
    for i in y:
        if i not in dy:
            dy[i]=1
        else:
            dy[i]+=1
    
    return dx == dy
        
is_anagram("typhoon", "opython")
is_anagram("Alice", "Bob")

..............................................

#solution..................................................
# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)
............................................................
