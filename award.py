"""
Author: Sandeep R Patel
Data types and conditionals Statement AG Task 3

Prompt user to enter times for:
    swim, cycle and running
Calculate and print total time

Determine award depending on qualifying criteria
Use if, elif and else statements

"""

swim = int(input("Enter your swimming time in minutes: "))
cycle = int(input("Enter your cycle time in minutes: "))
run = int(input("Enter your run time in minutes: "))

total_time = swim + cycle + run
print(f"The total time taken to complete the triathlon was: {total_time} minutes.")

if (0<total_time<=100):
    award = "Provincial colours"
elif (101<=total_time<=105):
    award = "Provincial half colours"
elif (106<=total_time<=110):
    award = "Provincial scroll"
else:
    award = "No award"

print(f"The award for the triathlon time is: {award}.")

