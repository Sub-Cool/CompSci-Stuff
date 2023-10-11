# Code a game that allows two players to enter their details, which are then authenticated using a universal password.
# The password is 'quandale' and the game will only start if the password is entered correctly by both players.
# In the game, both players roll two six-sided dice.
# Calculate and output the points for each round and each player's total points.
# Allow the players to play 5 rounds.
# The player with the highest total points wins.
# If the total points are equal, allow each player to roll one die until one player gets a higher score.
# Output the winner's name and total points.

import random

# Function to get player details
def getDetails():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

# Function to authenticate player details
def authenticate(username, password):
    if password == "apple pie":
        return True
    else:
        return False

# Function to roll dice
def rollDice():
    whenToRoll = input("Press enter to roll the dice: ")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

# Function to calculate points
def calculatePoints(dice1, dice2):
    points = dice1 + dice2
    return points

# Function to calculate total points
def calculateTotalPoints(points):
    totalPoints = 0
    totalPoints += points
    return totalPoints

# Function to determine winner
def determineWinner(player1Points, player2Points):
    if player1Points > player2Points:
        print("Player 1 wins with a score of", player1Points)
    elif player2Points > player1Points:
        print("Player 2 wins with a score of", player2Points)
    else:
        print("It's a draw!")
        while player1Points == player2Points:
            player1Dice = random.randint(1, 6)
            player2Dice = random.randint(1, 6)
            if player1Dice > player2Dice:
                print("Player 1 wins with a score of", player1Dice)
                break
            elif player2Dice > player1Dice:
                print("Player 2 wins with a score of", player2Dice)
                break
            else:
                print("It's a draw!")
                continue

# Main program
def main():
    player1Points = 0
    player2Points = 0
    tplayer1Points = 0
    tplayer2Points = 0
    rounds = 0
    username1, password1 = getDetails()
    username2, password2 = getDetails()
    if not authenticate(username1, password1) or not authenticate(username2, password2):
        return 1
    print("Authentication successful!")
    while rounds < 5:
        input(f"{username1} press enter to roll the dice: ")
        dice1, dice2 = rollDice()
        print(f"{username1} rolled a", dice1, "and a", dice2)
        player1Points = calculatePoints(dice1, dice2)
        tplayer1Points = tplayer1Points + player1Points
        print(f"{username1} scored", player1Points, "points!")
        print(f"{username1} has", tplayer1Points, "points!")
        while dice1 == dice2:
            print("You rolled a double! Roll again!")
            dice1, dice2 = rollDice()
            print(f"{username1} rolled a", dice1, "and a", dice2)
            player1Points = calculatePoints(dice1, dice2)
            tplayer1Points = tplayer1Points + player1Points
            print(f"{username1} scored", player1Points, "points!")
            print(f"{username1} has", tplayer1Points, "points!")
        input(f"{username2} press enter to roll the dice: ")
        dice1, dice2 = rollDice()
        print(f"{username2} rolled a", dice1, "and a", dice2)
        player2Points = calculatePoints(dice1, dice2)
        tplayer2Points = tplayer2Points + player2Points
        print(f"{username2} scored", player2Points, "points!")
        print(f"{username2} has", tplayer2Points, "points!")
        while dice1 == dice2:
            print("You rolled a double! Roll again!")
            dice1, dice2 = rollDice()
            print(f"{username2} rolled a", dice1, "and a", dice2)
            player2Points = calculatePoints(dice1, dice2)
            tplayer2Points = tplayer2Points + player2Points
            print(f"{username2} scored", player2Points, "points!")
            print(f"{username2} has", tplayer2Points, "points!")
        rounds += 1        
    determineWinner(tplayer1Points, tplayer2Points)
    if tplayer1Points > tplayer2Points:
        print(f"{username1} wins with a score of", tplayer1Points)
    elif tplayer2Points > tplayer1Points:
        print(f"{username2} wins with a score of", tplayer2Points)
    else:
        print("It's a draw!")
        while tplayer1Points == tplayer2Points:
            player1Dice = random.randint(1, 6)
            player2Dice = random.randint(1, 6)
            if player1Dice > player2Dice:
                print(f"{username1} wins with a score of", player1Dice)
                break
            elif player2Dice > player1Dice:
                print(f"{username2} wins with a score of", player2Dice)
                break
            else:
                print("It's a draw!")
                continue

main()
