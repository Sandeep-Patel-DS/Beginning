"""
Author: Sandeep R Patel
Iteration Practical Task 1

Prompt user for input

while user input is not equal to -1
    increment counter by 1
    increment total by value of user input
    prompt user for another input

when user input equals -1, calculate the average
using total and counter variable

"""

#prompt user for input
user_input = int(input("Enter integer here: "))

#initialize variables
counter = 0
total = 0

#while loop
while (user_input != -1):
    counter +=1
    total += user_input
    user_input = int(input("Enter integer here: "))

#calculate average when input ==1
if (counter ==0):
    print("The first number entered was -1 and so there is no average to compute.")
else:
    print (f"The number of non -1 entered: {counter}.\nThe numbers have a total of {total}.\nThe average is {total/counter}.")

