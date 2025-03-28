"""
Implement a program that :
- Enables user to place an order
- Prompts them, one per line
- Stops when the user enters Ctrl + D / CTRL D NOT WORKING ON WINDOWS APPARENTLY, USING CTRL Z RETURN INSTEAD
- After each inputted item, display the total prefixed with a dollar sign
- Total formatted to two decimals
- Input case insensitive
- Ignore any input that is not in the dictionnary
- Assume every item on the menu will be titlecased
"""

def main () :

    items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0

    while True :
        try :
            order = input("Item: ")
            order = order.lower()
            order = order.title()
            if order in items :
                total += items[order]
                print(f"${total:.2f}")
            
        except EOFError :
            break

main()