import random
enemyTurn = random.randint(1,3)
yourTurn = raw_input("Type: Rock, Paper or Scissors ?> ")
if yourTurn == "Rock" or yourTurn == "rock":
    if (enemyTurn == 1):
        print("You tied, you both did the same move")
    if (enemyTurn == 2):
        print("You lose, the enemy's paper wrapped itself around your rock")
    if (enemyTurn == 3):
        print("You win, you crushed the enemy's scissors with your rock")
elif yourTurn == "Paper" or yourTurn == "paper":
    if (enemyTurn == 1):
        print("You win, you wrapped your paper around your enemy's rock")
    if (enemyTurn == 2):
        print("You tied, you both did the same move")    
    if (enemyTurn == 3):
        print("You lose, the enemy's scissors cut right trough your paper")
elif yourTurn == "Scissors" or yourTurn == "paper":
    if (enemyTurn == 1):
        print("You tied, you both did the same move")
    if (enemyTurn == 2):
        print("You win, you cut the enemy's paper with your scissors")
    if (enemyTurn == 1):
        print("You lose, the enemy's rock crushed your scissors")
else:
    print("I don't know what",yourTurn,"means")
