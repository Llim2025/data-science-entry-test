# create lists with different methods
numbers = [1, 2, 3, 4, 5]  # List of numbers - common way
fruits = ["apple", "banana", "cherry"]  # List of fruits
print(fruits)  # Display the modified list of fruits

# numbers2 = list(range(1, 6))  # List of numbers using range and constructor

# Get a value
print(numbers[1])  # Accessing the first element (index 0)
print(fruits[1])  # Accessing the second element (index 1)

print(len(numbers))  # Length of the list
print(len(fruits))  # Length of the list

fruits.append("orange")  # Adding an element to the end of the list
fruits.remove("apple")  # Removing an element from the list
fruits.insert(1, "kiwi")  # Inserting an element at a specific index
print(fruits)  # Display the modified list of fruits

fruits.sort()  # Sorting the list of fruits
print("sorted", fruits)  # Display the sorted list of fruits

fruits.sort(reverse=True)  # Reverse Sorting the list of fruits
print("reverse sorted", fruits)  # Display the reverse sorted list of fruits


fruits.reverse()  # Reversing the list of fruits
print("reverse", fruits)  # Display the reversed list of fruits

# change value
fruits[0] = "mango"  # Changing the first element
print("changed", fruits)  # Display the modified list of fruits
