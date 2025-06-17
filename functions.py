def greet(first_name, last_name):  # parameters
    print("Hello, World!")
    print("welcome to Python programming")


greet("Louis", "Lim")  # arguments - actual values

# 1 - performing a task
# 2 - calculating a value


def get_greeting(first_name, last_name):  # parameters
    return f"Hello, {first_name} {last_name}"  # return value


message = get_greeting("Louis", "Lim")  # arguments - actual values
print(message)  # print the returned value


def increment(number, by=1):  # default parameter
    return number + by


print(increment(2, by=1))  # keyword argument


def multiply(*numbers):  # *args - variable number of arguments
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4))
