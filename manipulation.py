"""

Author: Sandeep R Patel
Data Types and Conditionals - AG Task 1

Prompt and save user input sentence
Calculate and display the length of the string
Loop through the index number up until the end of the string
    check whether the string chracter is equal to the last string character
    if so replace with @
    otherwise leave as is
Print string with replacements
Print the last three letters of the string
Create a five letter word that is made of:
the first three characters and the last two chracters

"""

str_manip = input("Enter a sentence here, be creative: ")
print(f"Length of string is: {len(str_manip)}")

str_sub = ""

""" The below loop returns a @ to the new string if chracters is equal to the
final string character, otherwise adds original chracter to the string.
Alternatively, the replace method could be used."""
for i in range(len(str_manip)):
    if str_manip[i]==str_manip[-1]:
        str_sub+="@"
    else:
        str_sub+=str_manip[i]

print(str_sub)

print(str_manip[-1:-1-3:-1])

created_word=str_manip[:3]+str_manip[-2:]
print(created_word)
