# a tuple is a collection that is ordered and unchangeable. Allows duplicate members.
fruits = ("apple", "banana", "cherry")
fruits2 = tuple(("apple", "banana", "cherry"))  # Tuple of fruits

print(fruits, fruits2)

# remove / del tuple
del fruits2  # Deleting a tuple

# get length of tuple
print(len(fruits))  # Length of the tuple
# check if item exists in tuple


# a set is a collection that is unordered, unchangeable, and unindexed. No duplicate members.

fruits_set = {"apple", "banana", "cherry"}  # Set of fruits

print('Apples' in fruits_set)

fruits_set.add("orange")  # Adding an element to the set

print(fruits_set)  # Display the set of fruits

fruits_set.remove("banana")  # Removing an element from the set

print(fruits_set)  # Display the modified set of fruits

fruits_set.clear()  # Clearing the set

# delete set
# del fruits_set  # Deleting the set
