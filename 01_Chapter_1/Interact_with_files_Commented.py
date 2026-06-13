# Importing os module, os modules help us to interact with file & folders...
import os

# To Stores the directory path in a variable, Here, the program will access the Users folder
path = "C:/Users"

# To read the content from the folder
contents = os.listdir(path)

# To print the items 
for item in contents:
    print(item)