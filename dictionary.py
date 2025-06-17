# create dict

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person, type(person))  # Display the dictionary and its type

# Another way to create a dictionary
person2 = dict(name="Jane", age=25, city="Los Angeles")

print(person['name'])  # Display the second dictionary and its type
print(person.get('name'))  # Display the second dictionary and its type

# Adding a new key-value pair to the dictionary
person['phone'] = "123-456-7890"
print(person)  # Display the updated dictionary

print("keys :", person.keys())  # Display the keys of the dictionary
print("values :", person.values())  # Display the values of the dictionary
# Display the items (key-value pairs) of the dictionary
print("items :", person.items())

person3 = person.copy()
person3.clear
print("len of person3", len(person3))  # Display the copied dictionary
print(len(person2))  # Display the copied dictionary

# list of dictionaries
people = [
    {"name": "Alice", "age": 28, "city": "Chicago"},
    {"name": "Bob", "age": 32, "city": "San Francisco"},
    {"name": "Charlie", "age": 25, "city": "Miami"}
]

print(people)  # Display the list of dictionaries
