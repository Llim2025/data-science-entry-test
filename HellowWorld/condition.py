temp = 35
if temp > 30:
    print("Its warm")
    print(":Drink water")
elif temp > 20:
    print("Its nice")
    print(":Enjoy the weather")
else:
    print("Its cold")
    print(":Wear a jacket")


age = 22
if age >= 18:
    message = "You are an adult"
else:
    message = "You are a minor"

message = "Eligible to vote" if age >= 18 else "Not eligible to vote"
# tenary operator

print(message)


high_income = True
good_credit = True
student = False

# true true false. left to right evaluate false - short circuiting
if high_income or good_credit and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

age = 22
if 18 <= age < 65:  # chaining comparison operators
    # if age >= 18 and age < 65:  #same
    print("Eligible to vote")

for number in range(1, 10, 2):  # start from 1 to 10, step by 2
    print("Attempt ", number + 1, (number + 1) * ".")

successful = False  # false option
for number in range(3):  # range is iterable
    print("Attempt ", number + 1, (number + 1) * ".")
    if successful:
        print("Successful")  # same indent for if successful
        break
else:
    print("Attempted 3 times and failed")

command = ""
while command.lower() != "quit":  # while loop
    command = input(">")
    print("ECHO", command)


# command = ""
# while True:  # infinite loop
#    command = input(">")
#    if command.lower() == "quit":quit

#        break
#    print("ECHO", command)
quit
count = 0
for number in range(10):  # range is iterable
    # if number % 2 == 0:
    # count += 1
    print("Even number:", number)  # same indent for if successful
print("Count of even numbers:", count)
