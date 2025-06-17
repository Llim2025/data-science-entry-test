
"""
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
"""

# Step 1 - Create a function to check if the number (num) is divisible by another number (divisor).


def check_divisibility(num, divisor):

    # Step 2 - Both num and divisor must be numeric.
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise ValueError("Both num and divisor must be numeric.")

    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")

# step 3 - Return True if num is divisible by divisor, False otherwise by using modulo function.
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))  # Output: True
print(check_divisibility(7, 3))   # Output: False
