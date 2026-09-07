print("================================")
print("Welcome Here")
print("My first post")
print("================================")

#a. Does the program display messages exactly as written?
# Yes
#b. What is the order of execution of the statements? top to bottom or bottom to top?
# top to bottom
#c. Where does the output appear?
# In the terminal

username = "cool_creator"
bio = "Fun Blogger"
followers = 100
print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)

#a. What is the use of the variables “username”, “bio” and “followers”?
# Store resusable values
#b. What if you change these values, does the output change?
# Yes


followers += 50

print("Day 1:", followers)

followers += 20

print("Day 2:", followers)

followers -= 10

print("Day 3:", followers)

#a. Do we manually have to reassign the follower value?
# No
#b. Does each operation affect the first value (100) or the existing value of followers?
# Yes
#c. What is the use of += or -= operators?
# To add/subtract from the inital value 

username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("====================")
print("Username: ", username)
print("Age: ", age)
print("Category: ", category)

#a. How does input() captures user’s input
# The program pauses and allows the user to type
#b. Is the program dynamic now or still hard coded?
# dynamic
#c. Try to run multiple types with different inputs

if age>40 and category == "fun":
    print("You are old what is fun for you?")

#a. What is the return type for input()
# String
#b. How are different conditions being checked?
# It checks if the conditions in the if statement is true and executes it, if false it ignores it
