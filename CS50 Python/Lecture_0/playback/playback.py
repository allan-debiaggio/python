def main() :
    # Taking input, removing spaces, creating a list of words
    words = input("Hey, what's up ?\n").split()

    sentence(words)

# Printing the sentence word by word
def sentence(words):
        for word in words :
            print(f"{word}",end="...")

main()