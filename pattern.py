"""
Author: Sandeep R Patel
Iteration Practice Task 2

pattern consists of a sequence of *
the pattern increases by one * up to and including 5*
thereafter the number of *'s goes down by 1
use loop with if statement to make asterix a function of index number
index values which are greater than 5,
should have asterix number be a function of index reversed

"""

for index in range (1,10):
    if (index<=5):
        print(index * "*")
    else:
        print((10-index) * "*")