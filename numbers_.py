"""
Author: Sandeep R Patel
Data Types and Conditional Statements AG Task 2

Prompt user to enter three different integers
Print
    Sum of all numbers
    First number - second number
    Third number * first number
    Sum of all / third number

"""

num1 = int(input("Enter your first integer here: "))
num2 = int(input("Enter your second integer here: "))
num3 = int(input("Enter your third integer here: "))

number_list=[num1,num2,num3]
print(f"Numbers entered by user: {number_list}")

print(sum(number_list))
print(num1-num2)
print(num3*num1)
print(sum(number_list)/num3)
