def main() :
    words = input("Hey, what's up ?\n").split()
    sentence(words)

def sentence(words):
        for word in words :
            print(f"{word}",end="...")

main()