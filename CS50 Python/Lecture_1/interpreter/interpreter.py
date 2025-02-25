"""
Implement a program that :
- Prompts the user for an arithmetic expression
- Calculates and outputs the result as a floating-point value formatted to one decimal place
Assume the input will be formatted as "x y z" with one space between x and y and one space between y and z
wherein :
x is an integer
y is +, -, * or /
z is an integer
"""

def main():

    number = input("Expression : ").split()
    print(f"{interpreter(number):.1f}")

def interpreter(expression) :

    number1 = float(expression[0])
    number2 = float(expression[2])
    
    if expression[1] == "+" :
        return float(number1 + number2)        
    elif expression[1] == "-" :
        return float(number1 - number2)
    elif expression[1] == "*" :
        return float(number1 * number2)
    elif expression[1] == "/" :
        return float(number1 / number2)
    else :
        message = "I didn't understand your expression"
        return message

main()