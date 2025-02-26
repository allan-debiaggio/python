"""
Implement a program that :
- Prompts the user for the name of a variable in camelCase
- Outputs the corresponding name in snake_case
"""

def main():
    
    name = []
    name += input("camelCase : ")
    print(snake_case(name))



def snake_case(text):

    # Creating a new list to store the text inputted and a count for the new index
    new_name = []
    new_name += text
    count = 0

    # Looping through every letter of the list
    for _ in range(len(text)):

        if text[_].isupper():
            # Inserting the "_" in existing list, using count to adapt to its new length
            new_name.insert(_ + count, "_")
            count += 1

    # Lowering letters in the final name and assembling a string with the list
    new_name = "".join(new_name).lower()

    return new_name



main()