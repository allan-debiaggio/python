# Prompts user for input, calls convert on that input, prints the result.
def main():
    user = input("")
    print(convert(user))
    
# Returns same string with any :) replaced with 🙂 and :( to 🙁
def convert(words):
   words = words.replace(":)", "🙂")
   words = words.replace(":(", "🙁")
   return words
        
main()