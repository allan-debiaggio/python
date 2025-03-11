def main():
    x = get_int("What's x ? ")
    print(f"x is {x}")

def get_int(prompt):    
    while True :
        try : 
            x = int(input(prompt))
        except ValueError :
            print("This is not an integer. Try again !")
            # pass / For not having the error printing, just the program looping
        else : 
            return x

main()