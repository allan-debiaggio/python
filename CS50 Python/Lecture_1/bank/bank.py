""" 
Implement a program that promopts the user for a greeting. 
If the greeting starts with "hello", output $0.
If the greeting starts with an "h", but not hello, output $20.
Otherwise, output $100.
Ignore any leading whitespace in the user's greeting,
Treat the user's greeting case-insensitively.
"""

def main():

    greeting = input("Greeting : ")
    check_greeting(greeting)


def check_greeting(sentence) :

    sentence = sentence.strip().lower()

    if sentence.startswith("hello") :
        print("$0")
    elif sentence.startswith("h"):
        print("$20")
    else :
        print("$100")


main()