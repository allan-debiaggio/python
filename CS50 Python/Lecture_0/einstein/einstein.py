# Prompt the user for mass as an integer (in kg) and outputs the equivalent of Joules as integer.

def main():
    number = int(input("Mass (kg) = "))
    print(f"Energy = {einstein(number)}")

def einstein(number):
    return number*300000000**2

main()