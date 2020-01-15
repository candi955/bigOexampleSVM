# This page is practice on lists, sets, Big O, and a little on linked lists

# References are listed, although much of what is referenced was modified into functions by myself for further
# exploration of the subjects

# reference for this study of lists, sets, and O(n) or Big O:
# https://www.youtube.com/watch?v=rfvc66Qog4o
# Although referenced, the functions at the end were edited/adjusted by me to fit
# some of my own study needs for arguments and efficiency on how I might want a function
# to occur during any future efforts

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

# _______________________________________________________________________________________________________________
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
# _______________________________________________________________________________________________________________
# if add to set, takes elements into consideration, and doesn't necessarily add the element as new to the set if
# it is already there

setlist.add(3)
print(setlist)
print("\n")

# result:
# {1, 3, 4}
# _______________________________________________________________________________________________________________
# because of this, we can remove duplicate elements from the set

setlist.remove(1)
print(setlist)
print("\n")

# result:
# {3, 4}
# _______________________________________________________________________________________________________________
# We only want to do a 'set' rather than a list, if we care about where the elements do and do not exist
# Sets can contain both numbers and strings

setlist = {1, 3, 'apple', 6, 9}
print(setlist)
print('\n')

# result:
# {1, 'apple', 3, 6, 9}
# _______________________________________________________________________________________________________________
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
# _______________________________________________________________________________________________________________
# 'Time Complexity of Sets versus Lists' _____________________________________________________________________


# result:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# searching in list of 0 - 24
print('Searching for element in list of 0-24:\n')
#create a list:

list = [x for x in range(25)]
print('Here is the list:')
print(list)
print('\n')

def _lookingForElementOnList_(list, lookingForListNum):  # is O(n), a linear function for the search
                                                        # because must look at all items on list

    for i in list:
        if i == lookingForListNum:
            while True:
                try:
                    print('It matches')

                except ValueError:
                    print("This didn't work")
                else:
                    break

        if i != lookingForListNum:
            while True:
                try:
                    i + 1

                except ValueError:
                    print('Error was made')
                else:
                    break



# creating set of 0 - 24
print('Searching for element in a set of 0-24:\n')
# (note: although some of this is from reference, some I created myself)
# # searching in set of 0 - 24

print('Here is the set:')
set1 = {x for x in range(25)}
print(set1)
print('\n')

# creating search function for set search.
# Please note: Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This
# enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
# reference for Enumerate(): https://www.google.com/search?q=what+is+enumerate+python&oq=what+is+enumerate+python&aqs=chrome..69i57j0l7.4103j0j7&sourceid=chrome&ie=UTF-8

def _didntwork_():
    print('That did not work')

def _lookingForNumInSet_(set1, lookingFor):  # is O(1) for Big O - able to find elements faster because
                                            # don't have to look through every element to find one
    if lookingFor in set1:
        print('A match was found')
    else:
        print('no match')


# calling function to look for list elements
print('For 12 on the List:\n')
_lookingForElementOnList_(list, lookingForListNum=12)
print('\n')

print('For 100 on the List:\n')
_lookingForElementOnList_(list, lookingForListNum=100)
print('\n')

# calling function to look for set numbers (elements)

print('Searching for 31 on the Set:\n')
_lookingForNumInSet_(set1, lookingFor=31)
print('\n')

print('Searching for 8 on the Set:\n')
_lookingForNumInSet_(set1, lookingFor=8)
print('\n')

# results:
# Here is the list:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# Searching for element in a set of 0-24:
# Here is the set:
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}
# For 12 on the List:
# It matches
# For 100 on the List:
# Searching for 31 on the Set:
# no match
# Searching for 8 on the Set:
# A match was found


# _______________________________________________________________________________________________________________
# Please note that for Big O, lists are considered O(n) for insert and removal (lists are slower for
# adding and removal; need index, n depends on amount of data) - have to look through entire list to
# see if element exists O(n), a linear function - basically how long it takes to find if element exists

print('Inserting on List 50 into the index 12, and 3 into the index 0 -- the front of the list')
list.insert(12,50)
print(list)
list.insert(0,3)
print(list)

# results
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 50, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# [3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 50, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


# _______________________________________________________________________________________________________________
# creating function with argument 'list':
def _listInsert_(list):
    print(list)

print('Implementing argument function for "list" adjustment')
print('full list:')
_listInsert_(list)
print('adjusted list:')
_listInsert_(list=(6, 10, 12))

# results
# Implementing argument function for "list" adjustment
# full list:
# [3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 50, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# adjusted list:
# (6, 10, 12)

# Please note that for Big O, sets are considered O(1) for insert and removal (sets are faster for adding or removal).
# It takes only one operation to see if element is on list.

# _______________________________________________________________________________________________________________

# Again for lists, removing the 10 and the 5 as below with list.remove is O(n) .. slower than O(1) like with sets
print('\nRemoving the 10 and 5 from the List:')
list.remove(10)
list.remove(5)
print(list)
print('\n')

# appears can't add to list, only insert


# Now will look at sets
print('\nRemoving the 10 and 5 from the Set, and adding 1000:')
set1.remove(10)
set1.remove(5)
set1.add(1000)

print(set1)
print('\n')

# It appears insert does not work on sets

# results:
# Removing the 10 and 5 from the List:
# [3, 0, 1, 2, 3, 4, 6, 7, 8, 9, 11, 50, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]#
# Removing the 10 and 5 from the Set, and adding 1000:
# {0, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1000}


# _______________________________________________________________________________________________________________

# More notes about sets:
# Reasons to utilize sets instead of lists:
# 1) Want to know if element exists, don't care how many, order, etc
# 2) When looking for unique elements or add and remove despite location
# 3) Determining multiple or duplicate elements


# How to determine if there are duplicates on a list (convert it to a set first):
newlist = [3, 5, 8, 2, 3, 2, 1, 1, 3, 2, 7]
print("Here is a new list:")
print(newlist)
print('\n')

listAsSet = set(newlist)
print('\n')

print("Here is the new list converted to a set:")
print(listAsSet)
print('\n')

# convert to set and check length of set versus length of original list
dup = len(listAsSet) == len(newlist)

print('Following will state if the lists are duplicate:')
print(dup)
print('\n')

dup = len(listAsSet) != len(newlist)

print('Following will state if the lists are different:')
print(dup)
print('\n')

# results:
# Here is a new list:
# [3, 5, 8, 2, 3, 2, 1, 1, 3, 2, 7]
# Here is the new list converted to a set:
# {1, 2, 3, 5, 7, 8}#
# Following will state if the lists are duplicate:
# False#
# Following will state if the lists are different:
# True

# Side note: converting a set to a list is O(n) because have to go through all elements of list to convert

# _______________________________________________________________________________________________________________

# A little look at linked lists: below is inserting a tail of a linked list from HackerRank
# reference: https://stackoverflow.com/questions/35559632/insert-a-node-at-the-tail-of-a-linked-list-python-hackerrank
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def Insert(head, data):
        if (head == None):
            head = Node(data)
        else:
            current = head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
            return head






