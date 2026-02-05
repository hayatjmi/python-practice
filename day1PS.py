# Level 1
# Question 1
channel_name = "code_logic_hub"
print("Welcom to "+ channel_name)

# Question 2
name = input("Enter Your Name:")
print("Hello "+ name)

# Question 3
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = int(num1)+int(num2)
sub = int(num1)-int(num2)
mul = int(num1)*int(num2)
print(sum)
print(sub)
print(mul)

# Level 2
# Question 4
num = input("Enter the number: ")
if int(num)%2 == 0:
 print("Even")

else:
 print("Odd") 

#  Question 5
age = input("Enter your age: ")
if int(age)>18:
 print("Permission Granted!")

else:
 print("Permission Denied !")  


# Question 6
for i in range(1,11):
 print(i)

# Or
count =1
while count<=10:
 print(count) 
 count +=1


#  LEVEL 3
#  Question 7
technologies = ["html","css","python"]
technologies.append("flask")
technologies.remove("css")
for item in technologies:
 print(item)

# Question 8
str = input("Enter Your Full Name: ")
print(str)
print(str.upper())
print(str.lower())
print(str.replace("k","n"))
print(len(str))

# Question 9
correct_username = "admin"
correct_password = "12345"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == correct_username and password == correct_password:
    print("Credential Successful")

else:
    print("Unsuccessful Credential")


# Question 10 
print("1. HTML")
print("2. CSS")
print("3. PYTHON")

choice= input("Enter your choice in range 1 to 3: ")
if choice == "1":
    print("You Choose HTML")
elif choice == "2":
    print("You choose CSS")
elif choice == "3":
    print("You choose PYTHON")
else:
    print("Invalid Choice")            