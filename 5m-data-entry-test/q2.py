"""
Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
"""

# Step 1 - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).


def find_and_replace(lst, find_val, replace_val):
    #  Step 2 - lst must be a list.
    if not isinstance(lst, list):
        print("Error: The first argument must be a list.")
        return []

    # Replace all occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

# Step 3 - Return the modified list
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# Output has returned [1, 5, 3, 4, 5, 5]
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))

# Output has returned ["orange", "banana", "orange"]
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
