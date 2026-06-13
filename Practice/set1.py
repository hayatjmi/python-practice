# Set Practice Questions
# Create a set of 5 numbers.
my_set = {1,2,3,4,5,8 }
your_set ={4,5,6,7,8}
print(my_set)
print(type(my_set))


# Add a new element to a set.
my_set.add('hello')
print(my_set)


# Remove an element from a set.
my_set.remove(3)
print(my_set)


# Find the union of two sets.
print(my_set.union(your_set))


# Find the intersection of two sets.
print(my_set.intersection(your_set))


# Find the difference between two sets.
print(my_set.difference(your_set))      # Understand what is the difference doning in this 


# Check whether an element exists in a set.
if 5 in my_set:
    print("yes,Exist")


# Remove duplicate values from a list using a set.
my_list = [ 1,2,2,3,3,4,4,5,5]
new_set = set(my_list)
print(new_set)
print(type(my_set))


# Find the length of a set.
print(len(new_set))


# Clear all elements from a set.
new_set.clear()
print(new_set)
print(len(new_set))