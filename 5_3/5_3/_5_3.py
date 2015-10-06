import re
import sys
while True:
  print("Cryptograph")  #a ascii = 97 | z ascii = 122 
  stri = raw_input("Text>") #A ascii = 65 | Z ascii = 90
  shift = int(input("Shift letters by>"))
  length = len(stri)
  counter = 0

  while counter != length:
    currentChar = int(ord(stri[counter]))
    if re.search(r'[a-z]', stri[counter]):
        changeChar = currentChar + shift
        while changeChar >= 123:
            diff = changeChar - 122
            changeChar = 96 + diff
    elif re.search(r'[A-Z]', stri[counter]):
        changeChar = currentChar + shift
        while changeChar >= 91:
            diff = changeChar - 90
            changeChar = 64 + diff

    else:
        changeChar = currentChar
    sys.stdout.write(chr(changeChar))
    counter = counter + 1
  sys.stdout.write("\n")
  break