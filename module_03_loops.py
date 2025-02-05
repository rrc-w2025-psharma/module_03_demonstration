"""
Description: Introduction to Loops
Author: Pirncepreet Sharma
Date: 4 February 2025
Usage: To execute, press the play button in the VSC IDE.
"""

# Variables used in this demonstration:
fruits = ["apple", "orange", "banana", "cherry"]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# FOR LOOP
# Iterate the collection
# Fruit is a new temporary variable which is 
# Available only in the for loop block.
myna = 1 
for fruit in fruits:
    print(fruit)
    myna += 1
    print(myna)

for i in range (10):
    print(i)

for i in range(2,8):
    print(i)

for i in range(1, 10, 2):
    print (i)
    
for i in range(-10, 0):
    print(i)
# INPUT FUNCTION
"""
name = input("What is your name?")
salary = float(input("What is your salary?"))

print(f"Name: {name} \nSalary: ${salary:,.2f}")
"""

# WHILE LOOP
"""
favourite_number = 0
while favourite_number < 100:
    favourite_number = int(input("Enter your favourite number, (not 7),100 and up to quit: "))
    if favourite_number == 7:
        print("You broke the game!!!")
        break
else:
    print("Your number is over 100")
"""

# LOOP CONTROL STATEMENTS

# CONTINUE:
for number in range(1, 10):
    # Use continue statement to skip over multiples of 3.
    if number % 3 == 0:
        continue
    # Print all other integers
    print(number)

#BREAK:
"""
# Use a for loop to iterate over the range of integers 
for number in range(1, 10):
    # Use the break statement to exit the loop if the integer is greater than 5
    if number > 5:
        break
    # Print all other integers.
    print(number)
"""

# INFINITE LOOP

# <ctrl> + c (in the terminal window) to stop an infinite loop in VS Code.
number = 10
while number > 0:
    number += 1
    if number > 100:
        break

# NESTED LOOP
# matrix variable defined at top of editor.
for row in matrix:
    for element in row:
        print(element, end = " ")
    print()