"""
Implement a program that : 
- Prompts the user for items (One per line) until the user inputs CTRL + D
- Output the user's grocery list in all uppercase
- The list must be sorted alphabetically by item
- Prefix each item with the number of times the user inputted that item
- No need to pluralize the items
- Treat user input case-insensitively
ALMOST WORKING, JUST NEEDS TO REMOVE THE MULTIPLE OCCURENCES IN THE FINAL LIST
"""

def main():
    groceries = []

    while True :
        try :
            item = input("")
            item = item.upper()
            groceries.append(item)

        except EOFError :
            groceries.sort()

            # for _ in groceries :
            #     if groceries.count(_) > 1 :
            #         groceries.remove(_)


            for item in groceries :
                    print(f"{groceries.count(item)} {item}")
            break

main()