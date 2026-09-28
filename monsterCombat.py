"""
Isabel Myers
Monster Combat - Turn Based RPG
"""

import random


class Fight:
    # Constructor to initialize the fight with random monster HP and starting player stats
    def __init__(self):
        # Randomly select monster's starting HP between 40 and 60
        self.monsterHp = random.randint(40, 60)
        self.monsterMaxHp = self.monsterHp

        # Initialize player's HP
        self.playerHp = 25
        self.playerMaxHp = 25

        # Initialize combat modifiers
        self.poison = 0
        self.allyCount = 0
        self.allyActive = False

    # Method for player to attack the monster
    def attack(self):
        attackList = [4, 6, 6, 8, 10, 10]
        damage = random.choice(attackList)
        self.monsterHp -= damage
        print(f"You attack the monster for {damage} damage!")

    # Method for player to heal themselves
    def heal(self):
        healAmount = random.randint(3, 8)
        self.playerHp += healAmount

        if self.playerHp > self.playerMaxHp:
            self.playerHp = self.playerMaxHp

        print(f"You heal yourself for {healAmount} HP! Current HP: {self.playerHp}")

    # Method for player to recruit an ally
    def ally(self):
        self.allyActive = True
        self.allyCount += 1
        print("You recruit an ally to help you!")

        if self.allyCount == 3:
            self.monsterHp -= 10
            print("Your ally deals a powerful 10 damage to the monster!")

    # Method for player to poison the monster
    def poisonAttack(self):
        poisonAdd = random.randint(2, 5)
        self.poison += poisonAdd
        print(f"You poison the monster! Poison level: {self.poison}")

    # Method for monster to attack the player
    def monsterAttack(self):
        damage = random.randint(2, 6)

        if self.allyActive:
            reduction = random.randint(1, 3)
            damage -= reduction
            if damage < 0:
                damage = 0
            print(f"Your ally blocks some damage! Reduction: {reduction}")
            self.allyActive = False

        self.playerHp -= damage
        print(f"The monster attacks you for {damage} damage! Your HP: {self.playerHp}")

        if self.poison > 0:
            self.monsterHp -= self.poison
            print(f"The poison deals {self.poison} damage to the monster!")
            self.poison -= 1


# Runs a single fight from start to finish
# Returns "win" or "loss" so main() can track the overall record
def playRound(gameFile, roundNumber):
    fight = Fight()

    print(f"Round {roundNumber}")
    print("A fierce Dragon appears before you!")
    print(f"Your HP: {fight.playerHp}")
    print(f"Monster HP: {fight.monsterHp}/{fight.monsterMaxHp}")
    print()

    gameFile.write(f"Round {roundNumber} started\n")

    while True:
        print(f"Your HP: {fight.playerHp}/{fight.playerMaxHp}")
        print(f"Monster HP: {fight.monsterHp}/{fight.monsterMaxHp}")

        if fight.poison > 0:
            print(f"Monster is poisoned! (Level {fight.poison})")
        if 0 < fight.allyCount < 3:
            print(f"Ally summoned {fight.allyCount} time(s)")
        if 0 < fight.monsterHp < 10:
            print("The monster is almost dead!")

        print()
        print("Choose your action:")
        print("1 - Attack")
        print("2 - Heal")
        print("3 - Ally")
        print("4 - Poison")

        choice = input("Enter your choice (1-4): ")
        print()

        # Keep asking until the player enters a valid choice
        while choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please enter a number from 1 to 4.")
            choice = input("Enter your choice (1-4): ")
            print()

        if choice == "1":
            fight.attack()
            gameFile.write("Attack\n")
        elif choice == "2":
            fight.heal()
            gameFile.write("Heal\n")
        elif choice == "3":
            fight.ally()
            gameFile.write("Ally\n")
        elif choice == "4":
            fight.poisonAttack()
            gameFile.write("Poison\n")

        print()

        if fight.monsterHp <= 0:
            print("VICTORY! You have defeated the Dragon!")
            gameFile.write(f"Round {roundNumber}: Player Won\n")
            return "win"

        fight.monsterAttack()
        print()

        if fight.playerHp <= 0:
            print("DEFEAT! You have been defeated by the Dragon...")
            gameFile.write(f"Round {roundNumber}: Monster Won\n")
            return "loss"


# Main function to run the game, including replay and the win/loss record
def main():
    gameFile = open("gamelog.txt", "w")

    print("WELCOME TO MONSTER COMBAT!")
    print()

    wins = 0
    losses = 0
    roundNumber = 1

    playing = True
    while playing:
        result = playRound(gameFile, roundNumber)

        if result == "win":
            wins += 1
        else:
            losses += 1

        roundNumber += 1

        print()
        print(f"Record so far: {wins} wins, {losses} losses")
        again = input("Play another round? (y/n): ").strip().lower()
        print()

        if again != "y":
            playing = False

    print(f"Final record: {wins} wins, {losses} losses")
    gameFile.write(f"Final record: {wins} wins, {losses} losses\n")
    gameFile.close()


main()