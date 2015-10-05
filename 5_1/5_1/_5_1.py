userInput = raw_input("Input>")
length = len(userInput)
counter = 0
character = length - 1
userOutput = ""
while counter != length:
    userOutput = userOutput + userInput[character]
    character = character - 1
    counter = counter + 1
print userOutput

