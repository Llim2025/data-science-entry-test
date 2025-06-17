
# create class

class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        return f"Hello, my name is {self.name}."  # return a f string

    def info(self):
        return f"{self.name} is {self.age} years old."
# create an instance of the class


brad = User("Brad", 'brad@gmail.com', 30)
print(type(brad))  # <class '__main__.Person'>
print(brad.greet())  # Hello, my name is John.
print(brad.info())  # John is 30 years old and lives in New York.


# extend class
class Customer(User):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance
        return f"Balance for {self.name} is set to {self.balance}."

    def greet(self):  # override the greet method from parent class
        # return a f string
        return f"Hello, my name is {self.name} and my balance is {self.balance}"
# create an instance of the Customer class


# init Person class
janet = Customer("Janet", "janet@mail.com", 54)
# init Customer class
print(type(janet))  # <class '__main__.Customer'>
print(janet.greet())  # Hello, my name is Janet and my customer ID is C12345.
janet.set_balance(1000)
print(type(janet))  # <class '__main__.Customer'>
print(janet.greet())  # Hello, my name is Janet.
