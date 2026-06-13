# Dictionary Practice Questions
# Create a dictionary containing name, age, and city.
my_dict = {"name":"Hayat", "age": 26, "city": "Saharanpur"}
my_dict["color"] = "red"


# Print the value of a specific key.
print(my_dict["name"])


# Add a new key-value pair.
my_dict.update({"roll":69})


# Update the value of an existing key.
my_dict.update({"color":"Green"})



# Delete a key-value pair.
my_dict.pop("roll")
print(my_dict)


# Print all keys of a dictionary.
print(my_dict.keys())


# Print all values of a dictionary.
print(my_dict.values())


# Check whether a key exists in a dictionary.
if "name" in my_dict.keys():
    print("exist")
else:
    print("not exist")


# Count the total number of key-value pairs.
print(len(my_dict))


# Take student details (name, roll number, marks) from the user and store them in a dictionary.
Stud_dict = {}
v=input("Enter the name : ")
Stud_dict["name"]= v

rN=input("Enter the roll number : ")
Stud_dict["roll number"]= rN

marks=input("Enter your marks : ")
Stud_dict["marks"]= marks

print(Stud_dict)
print(type(Stud_dict))


