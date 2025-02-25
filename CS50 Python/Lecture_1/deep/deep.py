"""Implement a program that prompts the user for the answer to the Great Question of Life, the Universe
and Everything.
- Outputs "Yes" if the user inputs "42" or (case insensitively) forty-two or forty two
- Outputs "No" otherwise
"""

def main():

    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything ? ")
    if check_answer(answer) :
        print("Yes")
    else :
        print("No")

def check_answer(text):

    text = text.lower()

    if "42" in text or "forty two" in text or "forty-two" in text :
        return True
        

main()