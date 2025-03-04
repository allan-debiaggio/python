name = input("What's your name ? ")

match name :
    case "Harry" | "Hermione" | "Ron": # Bars do the same thing as OR
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _ : # Handling all other cases
        print("WHO ???")

"""
Older version :

if name == "Harry" or "Ron" or "Hermione":
    print("Gryffindor")
elif name == "Draco" :
    print("Slytherin")
else :
    print("Who ?")
"""