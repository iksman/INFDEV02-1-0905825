import sys
i = 0
a = int(input("Number of lines> "))
spaces = a
asterixes = 1

spacesBackup = spaces
asterixesBackup = asterixes

while (i <= a):
    i = i + 1
    while (spaces != 0):
        sys.stdout.write(" ")
        spaces = spaces - 1
    spaces = spacesBackup
    while (asterixes != 0):
        sys.stdout.write("*")
        asterixes = asterixes - 1
    while (spaces != 0):
        sys.stdout.write(" ")
        spaces = spaces - 1
    spaces = spacesBackup - 2
    asterixes = asterixesBackup + 2
    spacesBackup = spaces
    asterixesBackup = asterixes
    sys.stdout.write("a\n")
sys.stdout.write("done")
        