"""
Author Sandeep R Patel
Prime Factor Program - captures prime numbers between 2 and 200

User inputs two numbers - (lets simplify and assume numbers are between 2 and 200)

Loop through numbers ranging between two numbers
    For each number, carry out a prime factor test***
    If number is prime add to list
    else do nothing
    next number in range
Repeat until all numbers in range have been tested
Output is prime factors between two numbers

*** Prime factor function
Accepts input
Checks whether number is divisible by 2
For operational speed, pre set a number of primes up to a certain bound (15)
Check whether number is divisible by primes in above list
Move on to more advanced tests ***

"""

def prime_test(a):
    divisors = [2,3,5,7,11,13]
    for prime in divisors:
        if (a==prime):
            return True
            break
        elif(a%prime==0):
            return False
            break
    

lower_bound = int(input("Enter the lower bound of your test range: "))
upper_bound = int(input("Enter the upper bound of your test range: "))

prime_list = []

for number in range(lower_bound,upper_bound+1):
    if (prime_test(number) != False):
        prime_list.append(number)
    else:
        pass
    
print(prime_list)



