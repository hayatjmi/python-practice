import os

path = "C:/Users"

contents = os.listdir(path)

for item in contents:
    print(item)