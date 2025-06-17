
"""
     Task 1
     - Create a function that reverses a given string (s).
     - s must be a string.
     - Return the reversed string.
"""

# Step 1 - Create a function that reverses a given string (s).


def string_reverse(s):

    # Step 2 - Check if s is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

# Step 3 - Return the reversed string by using slicing
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World"))  # Output: "dlroW olleH"
print(string_reverse("Python"))  # Output: "nohtyP"
