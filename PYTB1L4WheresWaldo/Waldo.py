
import random
Names = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(Names)

i = 1
for x in Names:
    print(x)
    print("Stoel Nr: ", + i)
    i += 1
    if x == "Waldo":
        break
