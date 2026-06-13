# Mixed Practice Questions (Interview/Exam Level)
# Store 5 student names in a list and their marks in a dictionary.
# students = []
# marks = {}

# for i in range(5):
#     name = input("Enter student name: ")
#     mark = int(input("Enter marks: "))

#     students.append(name)
#     marks[name] = mark

# print("Students:", students)
# print("Marks:", marks)


# Remove duplicate elements from a list and store them in a set.
numbers = [1, 2, 2, 3, 4, 4, 5, 5]

duplicates = set()

for num in numbers:
    if numbers.count(num) > 1:
        duplicates.add(num)

print(duplicates)

# Convert a tuple into a list, add an element, and convert it back to a tuple.
# Find common elements between two lists using sets.
# Create a dictionary where keys are student names and values are marks, then find the student with the highest marks.