my_list=['Mike','Jane','Alex',1000,200,2000,True,False]

# .append() - adds an item to the end of the list
my_list.append('John')
print(my_list)

# .insert() - adds an item at a specified index
my_list.insert(1,'Mary')
print(my_list)

# .pop() - removes an item at a specified index and returns it
my_list.pop(3)
print(my_list)

# task
lst=[10,20,30,['Jane','Mary',[1000,2000,3000]],40,50,60]

# Using methods:
# add 70 at the end of the list
lst.append(70)
print(lst)

# add 1500 btw 1000 and 2000
lst[3][2].insert(1,1500)
print(lst)

# delete 2000
lst[3][2].pop(2)
print(lst)

# OR lst[3][2].remove(2000)

# .sort() - used to arrange list itemms ascendingly by default
lst1=[1,50,10,20,5,2]
lst1.sort()
print(lst1)
lst1.sort(reverse=True) # to sort in descending order
print(lst1)

# remove() - removes the first occurrence of a specified value
lst2=['Mike','Jane','Alex']
lst2.remove('Alex')
print(lst2)

# extend() - adds all items of an iterable (list, tuple, set, etc.) to the end of the list
lst3=lst2+lst1
print(lst3)
lst2.extend(lst1)
print(lst2)

# count() - returns the number of times a specified value appears in the list
print(lst2.count('Mike'))

# copy() - returns a copy of the list
lst4=lst1.copy()
print(lst4)

# clear() - removes all items from the list
lst4.clear()
print(lst4)

# in membership operator - checks if a specified value is present in the list. Returns True if found, otherwise False.
print('Alex' in lst2)