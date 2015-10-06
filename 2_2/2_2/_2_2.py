import random
enemyTurn = random.randint(1,3)
print("RPSLS v1.0")
while True:
    yourTurn = raw_input("Type: Rock, Paper, Scissors Lizard or Spock?> ")
    if yourTurn == "Rock" or yourTurn == "rock":
        if (enemyTurn == 1):
            print("You tied, you both did the same move")
        if (enemyTurn == 2):
            print("You lose, the enemy's paper wrapped itself around your rock")
        if (enemyTurn == 3):
            print("You win, you crushed the enemy's scissors with your rock")
        if (enemyTurn == 4):
            print("You win, you crushed the enemy's lizard with your rock")
        if (enemyTurn == 5):
            print("You lose, the enemy's Spock vaporized your rock")
        break
    elif yourTurn == "Paper" or yourTurn == "paper":
        if (enemyTurn == 1):
            print("You win, you wrapped your paper around your enemy's rock")
        if (enemyTurn == 2):
            print("You tied, you both did the same move")    
        if (enemyTurn == 3):
            print("You lose, the enemy's scissors cut right trough your paper")
        if (enemyTurn == 4):
            print("You lose, the enemy's lizard eats your paper")
        if (enemyTurn == 5):
            print("You win, the enemy's Spock was disproved by your paper")
        break
    elif yourTurn == "Scissors" or yourTurn == "paper":
        if (enemyTurn == 1):
            print("You tied, you both did the same move")
        if (enemyTurn == 2):
            print("You win, you cut the enemy's paper with your scissors")
        if (enemyTurn == 3):
            print("You lose, the enemy's rock crushed your scissors")
        if (enemyTurn == 4):
            print("You win, the enemy's lizard was decapitated by your scissors")
        if (enemyTurn == 5):
            print("You lose, the enemy's Spock smashed your scissors")
        break
    elif yourTurn == "Lizard" or yourTurn == "lizard" :
        if (enemyTurn == 1):
            print("You lose, the enemy's rock crushed your lizard")
        if (enemyTurn == 2):
            print("You win, your lizard eats the enemy's paper")
        if (enemyTurn == 3):
            print("You lose, the enemy's scissors decapitated your lizard. I hope you weren't getting too attached to it")
        if (enemyTurn == 4):
            print("You tied, you both did the same move")
        if (enemyTurn == 5):
            print("You win, the enemy's Spock got poisoned by your lizard")
        break
    elif yourTurn == "Spock" or yourTurn == "spock":
        if (enemyTurn == 1):
            print("You win, your Spock vaporizes the enemy's rock")
        if (enemyTurn == 2):
            print("You lose, your Spock got disproven by the enemy's paper")
        if (enemyTurn == 3):
            print("You win, your Spock smashes the enemy's scissors")
        if (enemyTurn == 4):
            print("You lose, the enemy's lizard poisoned your Spock")
        if (enemyTurn == 5):
            print("You tied, you both did the same move")
        break
    else:
        print("I don't know what",yourTurn,"means")
