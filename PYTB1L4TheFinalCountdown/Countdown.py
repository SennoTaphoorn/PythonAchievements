
from PIL import Image
number = 1001
while number > 0:
    number -= 1
    print(number)
if number == 0:
     afbeelding = Image.open("Birky.png")
     afbeelding.show()
