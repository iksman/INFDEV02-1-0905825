import sys
import math
shape = raw_input("||1>A full square|| ||2>A hollow square|| ||3>A rectangle|| ||4>Isoceles|| ||5>A circle||\nCommand>")
if shape == "1" or shape == "2" or shape == "3" or shape == "4":
    height = int(raw_input("Height>"))

if shape == "5":
    circum = int(raw_input("Circumference>"))
result = ""
x = 0
counter = 0
done = False
if shape == "1":
    for i in range(height):
        for x in range(height):
            result = result + "*"
        result = result + "\n"
elif shape == "2":
    while counter != (height + 1):
        if counter == 0:
            for x in range(height):
                result = result + "*"
            result = result + "\n"
            counter = counter + 1
        elif counter == height:
            for x in range(height):
                result = result + "*"
            result = result + "\n"
            break
        elif counter != height - 1:
            result = result + "*"
            for x in range(1, height - 1):
                result = result + " "
            result = result + "*"
            result = result + "\n"
            counter = counter + 1
        else:
            counter = height
elif shape == "3":
    counter = 1
    while counter != height + 1:
        for x in range(0,counter):
            result = result + "*"
        result = result + "\n"
        counter = counter + 1
elif shape == "4":
    spaces = height - 1
    chars = 1
    while counter != height:
        while done == False:
            charpos = spaces + chars
            secondpos = spaces + chars
            for x in range(0, spaces):
                result = result + " "
            for x in range(spaces, charpos):
                result = result + "*"
            for x in range(charpos, secondpos):
                result = result + " "
            spaces = spaces - 1
            chars = chars + 2

            done = True
        counter = counter + 1
        result = result + "\n"
        done = False
elif shape == "5":
    for i in range(-circum, circum + 1):
        for j in range(-circum, circum + 1):
            if math.sqrt((i**2)+(j**2)) <= circum + 0.2:
                result = result + "*"
            else:
                result = result + " "
        result = result + "\n"
else:
    result = "I don't know what '" + shape + "' means!"      
print result