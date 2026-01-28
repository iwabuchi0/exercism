"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal" 
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if list_one in list_two:
        return SUBLIST
    if list_two in list_one:
        return SUPERLIST
    else:
        return UNEQUAL
    
def is_subsequence(small, large):
    if not small:
        return True
    if len(small) > len(large):
        return False
    
    for i in range(len(large) - len(small) + 1):
        if large[i:i+len(small)] == smal:
            return True
    return False

    
