"""
Implement a program that : 
- Prompts the user for a str of text
- Outputs the same text with all vowels (A,E,I,O,U) omitted
- Works in uppercase or lowercase
"""

def main() :

    user = input("Input : ")
    print(f"Output : {twttr(user)}")

def twttr(text) :
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    new_text = []
    new_text += text

    for _ in range(len(text)):
        if text[_] in vowels :
            new_text.remove(text[_])

    return "".join(new_text)

main()