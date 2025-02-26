"""
Implement a program that :
- Prompts the user to insert a coin (one at a time)
- Informs the amount due each time
- Once inputted, outputs how many is left
- Keeps running while remaining != 0
- Assume the user will only input integers
- Ignore any integer that isn't :
    25
    10
    5
"""

def main():
    
    coke()


def coke():

    remaining = 50
    accepted_coins = [25,10,5]

    while remaining > 0 :
        # Asking for coin and providing the amount left, taking an int as answer
        cents = int(input(f"Amount Due : {remaining}\nInsert Coin : "))

        if cents in accepted_coins :
            remaining -= cents
    
    if remaining < 0 :
        # Printing the absolute number to remove the negative sign and only keep the value
        print(f"Change Owed : {abs(remaining)}")
    
    else :
        print("Change Owed : 0")

main()
