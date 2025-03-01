"""
Implement a program that : 
- Prompts the user for a vanity plate
- Outputs Valid if meets all of the requirements
- Outputs Invalid if it doesn't
- Assume that any of the letters inputted will be uppercases
- Structure your program per the below, wherein :
    - is_valid returns True if "s" meets all requirements
    - is_valid returns False if it does not.
    - Assume that "s" will be a string.
- You're welcome to implement additional functions for "is_valid" to call (e.g., one function per requirement)

Requirements : 
1 - All vanity plates must start with at least two letters.
2 - Vanity plates may contain a maximum of 6 characters (letters or numbers), and a minimum of 2 characters
3 - Numbers cannot be used in the middle of a plate; they must come at the end. For example :
    - AAA222 would be an acceptable plate
    - AAA22A would not. 
4 - The first number used cannot be a 0
5 - No periods, spaces or punctuation marks are allowed
"""

def main() :
    plate = input("Plate : ")
    if is_valid(plate):
        print("Valid")
    else :
        print("Invalid")

def is_valid(s):
    if start_letters(s) and min_max(s) :
        return True

def start_letters(s): # Requirement 1
    if s[0].isalpha() and s[1].isalpha() :
        return True

def min_max(s): # Requirement 2
    if 2 <= len(s) <= 6 :
        return True

# def numbers_place(s) : # Requirement 3

# def first_number(s): # Requirement 4

# def punctuation(s) : # Requirement 5
     
        

main()