"""
Implement a program that :
- Prompts the user for a time
- Outputs whether it's "breakfast time", "lunch time" or "dinner time"
- If it's not time for a meal, don't output anything at all
- Assume that the input will be formatted in 24-hour time as #:## or ##:##
- Assume that each meal's time range is inclusive. For instance :
    7:00, 7:01, 7:59, 8:00 or anytime inbetween, it's time for breakfast

Structure your program as such :
- convert is a function that converts "time", a str in 24-hour format, to the corresponding number of hours
as a float. For instance : 
    7 : 30 = 7.5
"""

def main() :

    user = input("What time is it ? ").split(":")
    result = convert(user)
    if 7 <=  result <= 8 :
        print("breakfast time")
    elif  12 <= result <= 13 :
        print("lunch time")
    elif  18 <= result <= 19 :
        print("dinner time")



def convert(time) :

    number1 = float(time[0])
    number2 = float(time[1])

    return number1 + (number2 / 60)

if __name__ == "__main__" :
    main()