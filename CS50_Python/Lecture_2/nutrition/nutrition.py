"""
Implement a program that :
- Prompts users to input a fruit(case insensitively)
- Outputs the number of calories in one portion of that fruit
(per the FDA's poster for fruits, which is also available as text)
- Capitalization aside, assume that users will input fruits
exactly as written in the poster (e.g., "strawberries", not "strawberry")
- Ignore any input that isn't a fruit
"""
def main():

    user = input("Item : ").lower()
    get_calories(user)

def get_calories(fruit) :

    informations = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew melon" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80
    }

    if fruit in informations :
        print(informations[fruit])

main()