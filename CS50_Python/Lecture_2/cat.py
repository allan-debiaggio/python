def main() :
    number = get_number()
    meow(number)

def meow(times):
    for _ in range(times):
        print("meow")

def get_number() :
    while True :
        n = int(input("How many meows ? "))
        if n > 0 :
            return n

main()

"""
Version 3 : Now with loops

while True :
    n = int(input("What's n ? "))
    if n > 0 :
        break

for _ in range(n) :
    print("meow")
"""
    
"""
Version 2, one line but a bit too complex :

print("meow\n" * 3, end="")
"""

"""
First version :

user = int(input("How much meows ? "))

for _ in range(user) :
    print("meow")
"""