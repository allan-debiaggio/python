def main():
    print_square(5)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()

"""
6th example : 

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()
"""

"""
5th example : 

def main():
    print_square(3)

def print_square(size):

    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        print()

main()
"""

"""
Fourth example (Horizontal) :
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
"""

"""
Third example (Vertical) :

def main():
    print_column(3)

def print_column(height):
    # Other example : print("#/n" * height, end="")
    for _ in range(height):
        print("#")

main()
"""

"""
Second example :

for _ in range(3) :
    print("#")
"""

"""
First example :

print("#")
print("#")
print("#")
"""