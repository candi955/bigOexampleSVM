import re

# reference
# sets tutorial
# in curly brackets
# it's own unique data type
s = {1, 2, 3, 4, 4}

print(type(s))
print(s)
print("\n")

# result:
# <class 'set'>
# {1, 2, 3, 4}

# list
# in brackets
l=[1, 2, 3, 4, 5]
print(type(l))
print(l)
print("\n")

# result:
# <class 'list'>
# [1, 2, 3, 4, 5]

# list is ordered collection datatype that is mutable
# list is ordered, a set, although mutable,  is not ordered
# set doesn't support indexing, but isn't ordered via index

# sets only contain unique elements
# sets are unique, unordered, elements
setlist = {1, 1, 1, 3, 4}
print(setlist)
print("\n")

# results:
# {1, 3, 4}

# if add to set, takes elements into consideration, and doesn't necessarily add the element as new to the set if
# it is already there

setlist.add(3)
print(setlist)
print("\n")

# result:
# {1, 3, 4}

# because of this, we can remove duplicate elements from the set

setlist.remove(1)
print(setlist)
print("\n")

# result:
# {3, 4}

# We only want to do a 'set' rather than a list, if we care about where the elements do and do not exist
# Sets can contain both numbers and strings

setlist = {1, 3, 'apple', 6, 9}
print(setlist)
print('\n')

# result:
# {1, 'apple', 3, 6, 9}

# a set doesn't actually present as 'ordered' necessarily (see example below once elements are added)

setlist.add(-8)
print(setlist)
print('\n')

setlist.add(5)
print(setlist)
print('\n')

setlist.add('peaches')
print(setlist)
print('\n')

# results:
# {1, 3, 6, 'apple', 9, -8}
# {1, 3, 5, 6, 'apple', 9, -8}
# {1, 'peaches', 3, 5, 6, 'apple', 9, -8}

# sets are fast though to find an element; can be thought of as 'constant' time

# 'Time Complexity of Sets versus Lists'
#create a list:

list = [x for x in range(25)]
print(list)
print('\n')

# result:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# searching in list of 0 - 24
print('searching for element in list of 0-24:')
lookingFor11 = 11

def _lookingfor11onList_():

    lookingFor11 = 11
    for i, el in enumerate(list):  # O(n) time is a linear function, can take a long time
        if el == lookingFor11:
            while True:
                print(lookingFor11)
                break

        elif el != lookingFor11:
            print('This number is not in the list')
            break


# creating set of 0 - 24
# (note: although some of this is from reference, some I created myself)
# # searching in set of 0 - 24

print('searching for element in set of 0-24:')
set = {x for x in range(25)}
print(set)
print('\n')

# creating search function for set search.
# Please note: Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This
# enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
# reference for Enumerate(): https://www.google.com/search?q=what+is+enumerate+python&oq=what+is+enumerate+python&aqs=chrome..69i57j0l7.4103j0j7&sourceid=chrome&ie=UTF-8
def _lookingForNumInSet_(set, lookingFor):

    for i, el in enumerate(set):
        if el == lookingFor:
            while True:
                print('This number is in the set:')
                print(lookingFor)
                break

        #elif el != lookingFor:
            #print('This number is not in the set')
            #break
        else:
            print('This number is not in the set')
            break


print('for the number not in set, 31:')
_lookingForNumInSet_(set, lookingFor={31})

print('for number in the set, 8:')
_lookingForNumInSet_(set, lookingFor={8})





