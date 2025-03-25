"""
Implement a program that : 

- Prompts the user for a fraction (formatted as X/Y, wherein each of X and Y is an integer)
- Then outputs, as a percentage rounded to nearest integer, how much fuel is left in the tank
- If 1% or less remains, outputs "E" to indicate empty.
- If 99% or more remains, outputs "F" to indicate full.
- If X or Y is not an integer, X > Y or Y == 0, prompt the user again.
- It is not necessary for Y to be 4
- Be sure to catch any exception like ValueError or ZeroDivisionError
"""

def main () :
    while True :
        try :
            user = input("Fraction : ")
            number1, number2 = separate(user)
            number1, number2 = integer(number1,number2)
            if number1 > number2 :
                continue
            print(percentage(number1, number2))
            break
        except ValueError :
            continue
        except ZeroDivisionError :
            continue
        except KeyboardInterrupt :
            print("Quitting program...\n")
            break

def separate(expression) :
    return expression.split(sep="/")

def integer(number1, number2) :
    return int(number1), int(number2)

def percentage(number1, number2) :
    result = round(number1 / number2 * 100)
    if result <= 1 :
        return "E"
    if result >= 99 : 
        return "F"
    else : 
        return f"{result}%"

main()