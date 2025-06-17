
"""
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
"""

# Step 1 - Create a function that updates a dictionary (dct) with a new key-value pair.


def update_dictionary(dct, key, value):

    if not isinstance(dct, dict):
        print("Error: The first argument must be a dictionary.")
        return {}

# Step 2 - If the key already exists in dct, print the original value, then update its value.
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    dct[key] = value

# Step 3 - Return the updated dictionary
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# Scenario 1: {}, "name", "Alice". Output: {"name": "Alice"}
my_dict = {}
updated_dict = update_dictionary(my_dict, "name", "Alice")
print(updated_dict)

# Scenario 2: {"age": 25}. output: {"age", 26}
my_dict.clear
my_dict = {"age": 25}
updated_dict = update_dictionary(my_dict, "age", 26)
print(updated_dict)
