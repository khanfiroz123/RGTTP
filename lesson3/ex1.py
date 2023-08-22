"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# when i used below:
# shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']
# it returns the below error:
# Traceback (most recent call last):
#  File "/home/fgadkano/git/RGTTP/lesson3/ex1.py", line 6, in <module>
#    shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']
#  TypeError: 'type' object is not subscriptable

# 1. Add banana to a shopping list.

# INSERT CODE HERE
shopping_list.append('banana')
print(shopping_list)

# 2. Add chocolate in the third position in your shopping list

# INSERT CODE HERE
shopping_list.insert(2, 'chocolate')
print(shopping_list)

# 3. Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

# INSERT CODE HERE

new_list = ['chocolate', 'carrot', 'avocado']
shopping_list.extend(new_list)
print(shopping_list)

# 4. Remove first chocolate only

# INSERT CODE HERE

idx: int = shopping_list.index('chocolate')
print(idx)
shopping_list.pop(idx)
print(shopping_list)

# 5. Remove last item from the list

# INSERT CODE HERE

shopping_list.pop()
print(shopping_list)


# 6. Remove third item from the list

# INSERT CODE HERE


shopping_list.pop(2)
print(shopping_list)


# 7. Count how many carrots are in the shopping list?

# INSERT CODE HERE


print(shopping_list.count('carrot'))
print(shopping_list)



# 8. Get the index of the chocolate (careful can throw traceback)

# INSERT CODE HERE

try:
    idx1: int = shopping_list.index('chocolate')
    print(idx1)
except ValueError as e:
    print(e)    
# 9. Get the index of carrot, make sure this code is executed

# INSERT CODE HERE
try:
    idx2: int = shopping_list.index('carrot')
    print(idx2)
except ValueError as e:
    print(e)