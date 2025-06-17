"""
     Task 1
     - Create a function that would swap the value of x and y using only x and y as variables.
     - x and y must be numeric.
     - Return -1 if x and y is not numeric, and
     - print the swapped values if both x and y are numeric.
"""

# Step1 - Create a function that would swap the value of x and y using only x and y as variables.


def swap(x, y):

    # Step 2 - Check x and y must be numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        # Step 3 - Return -1 if x or y is not numeric
        return -1

    x = x + y
    y = x - y
    x = x - y

# Step 4 - Print the swapped values
    print("Swapped values:", "x =", x, "y =", y)


# Tested outcome with the requested scenarios:
swap("Apple", 10)     # Output is silent as return is -1
swap(9, 17)           # Output is "Swapped values: x = 17 y = 9"
