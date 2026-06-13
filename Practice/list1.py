# List Practice Questions

# Store 5 favorite fruits in a list and print them.
"""
fruits = []
f1 = input("Enter fruit here: ")
fruits.append(f1)
f1 = input("Enter fruit here: ")
fruits.append(f1)
f1 = input("Enter fruit here: ")
fruits.append(f1)
f1 = input("Enter fruit here: ")
fruits.append(f1)
f1 = input("Enter fruit here: ")
fruits.append(f1)
f1 = input("Enter fruit here: ")
fruits.append(f1)

print(fruits) """


# Take 5 numbers from the user and store them in a list.
numbers=[]
f1 = int(input("Enter fruit here: "))
numbers.append(f1)
f1 = int(input("Enter fruit here: "))
numbers.append(f1)
f1 = int(input("Enter fruit here: "))
numbers.append(f1)
f1 = int(input("Enter fruit here: "))
numbers.append(f1)
f1 = int(input("Enter fruit here: "))
numbers.append(f1)

print(numbers)

# Find the largest element in a list.
print(max(numbers))

# Find the smallest element in a list.
print(min(numbers))
# Count how many times a number appears in a list.
print(numbers.count(3))
# Reverse a list.
rev_list = numbers[::-1]       # Understand the methods 1. new_list = reversed(list)   2. list.reverse()   3. Slicing list[::- 1]
print(rev_list)

# Sort a list in ascending order.
print(sorted(numbers))         #  Understand sort & sorted how they are used in python

# Add a new element at the end of a list.
numbers.append(99)
print(numbers)
# Remove a specific element from a list.
numbers.remove(3)
print(numbers)
# Find the sum of all elements in a list.
print(sum(numbers))