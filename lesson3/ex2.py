"""
  Lesson 3: ex2.py
"""

# 1. Create a list of number 0 to 9 using a for loop.
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# INSERT CODE HERE

mylist = []
for i in range(10):
    mylist.append(i)
print(mylist)


# 2. Create a list of number from 0 to 9 the power of 2 using a for loop.
#
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# INSERT CODE HERE
mylist1 = []
for i in range(10):
    mylist1.append(i**2)
print(mylist1)



# 3. Create a list of lists, which contains elements that are
# number, number(to the power of 2), number(to the power of 3)
#
# [[0, 0, 0], [1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64],
#  [5, 25, 125], [6, 36, 216], [7, 49, 343], [8, 64, 512],
#  [9, 81, 729]]

# INSERT CODE HERE

# mylist2: list[list[int]] = []
# newlist: list = []
mylist2 = []
for i in range(10):
    newlist: list = [i, i**2, i**3]
    mylist2.append(newlist)
print(mylist2)


# 4. Add condition in a for loop, that only numbers that are odd are added.
#
# [[1, 1, 1], [3, 9, 27], [5, 25, 125], [7, 49, 343], [9, 81, 729]]

# INSERT CODE HERE

# newlist1: list = []
mylist3 = []
for i in range(1, 10, 2):
    newlist1: list = [i, i**2, i**3]
    mylist3.append(newlist1)
print(mylist3)

# 5. Create a nested lists in a list with a for loop:
# [['ax', 'bx', 'cx', 'dx', 'ex'],
#  ['ay', 'by', 'cy', 'dy', 'ey'],
#  ['az', 'bz', 'cz', 'dz', 'ez']]

# mylist4 = []
newlist2 = []
for i in 'xyz':
    for j in 'abcde':
        newlist2.append([j+i])
    # newlist2.append([i+'y'])
    # newlist2.append([i+'z'])
    # mylist4.append(newlist2)
print(newlist2)




