import sys
shape = raw_input("||1>A full square|| ||2>A hollow square|| ||3>A rectangle|| ||4>Isoceles||\nCommand>")
height = int(raw_input("height"))
width = height

coolwidth = width - 1
coollength = height - 1
lines = height + 1
result = ""
x = 0
i = 0
counter = 0
done = False
if shape == "1":
    for i in range(height):
        for x in range(height):
            result = result + "*"
        result = result + "\n"
elif shape == "2":
    while counter != lines:
        if counter == 0:
            for x in range(width):
                result = result + "*"
            result = result + "\n"
            counter = counter + 1
        elif counter == height:
            for x in range(width):
                result = result + "*"
            result = result + "\n"
            break
        elif counter != coollength:
            result = result + "*"
            for x in range(1, coolwidth):
                result = result + " "
            result = result + "*"
            result = result + "\n"
            counter = counter + 1
        else:
            counter = height
elif shape == "3":
    counter = 1
    while counter != lines:
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
else:
    print "I don't know what",shape,"means!"        
print result