"""
Isabel Myers
Monster Combat - Turn Based RPG
"""
# Import a random number generator to allow the user to have
# a different experience each time they play
import random


class Fight:
    """
    My main and only class, this keeps the code organized by keeping the data and the
    methods that use it together. This is called encapsulation. It also makes it easy to
    add on to by possibly adding child classes if wanted in the future, which is inheritance.
    """
    def __init__(self):
        """
        Constructor, initializes all the variables that will be used within the other methods
        in the Fight class. This method runs automatically every time a new Fight object is
        created because it is called "__init__".
        """
        # randomly selects the monster's health between 40 and 60, inclusive.
        self.monsterHp = random.randint(40, 60)
        # sets the max health the monster can be at the initial health of the monster
        self.monsterMaxHp = self.monsterHp

        # set the user's health to 25 hp
        self.playerHp = 25
        # set the max hp of the user to 25
        self.playerMaxHp = 25

        # initializes the poison to start at 0
        self.poison = 0
        # initializes the ally count of the user to be 0
        self.allyCount = 0
        # sets the initial status of user allies to False
        self.allyActive = False

    def attack(self):
        """
        called when the user inputs '1' and chooses to attack the monster
        """
        # creates a list of numbers
        attackList = [4, 6, 6, 8, 10, 10]
        # chooses a random integer from the list of numbers
        damage = random.choice(attackList)
        # subtracts the random number chosen from the monster's hp
        self.monsterHp -= damage
        # prints out how much damage has been done to the monster
        print(f"You attack the monster for {damage} damage!")

    def heal(self):
        """
        called when the user inputs '2' and chooses to heal themselves
        """
        # choose a random amount to heal themselves between 3 and 8, inclusive
        healAmount = random.randint(3, 8)
        # adds random amount chosen to the user's hp
        self.playerHp += healAmount

        # below was a solution to one of my edge cases where the user's hp went
        # above their initial hp and kept increasing if they kept choosing to heal themselves

        # if the player's hp goes above their max hp it sets their hp to their max hp so it
        # cannot go over anymore
        if self.playerHp > self.playerMaxHp:
            self.playerHp = self.playerMaxHp
        # prints out how much the player heals themself for including any amount over but outputs their
        # health as their max health and not over
        print(f"You heal yourself for {healAmount} HP! Current HP: {self.playerHp}")

    def ally(self):
        """
        called when the user inputs '3' and chooses to recruit an ally
        """
        # sets 'true' to current ally
        self.allyActive = True
        # adds one ally to the ally counter
        self.allyCount += 1
        # prints out a statement saying they have gained an ally
        print("You recruit an ally to help you!")

        # if the ally count is 3 then the monster's hp decreases by 10
        if self.allyCount == 3:
            self.monsterHp -= 10
            # prints out the ally did 10 damage to the monster
            print("Your ally deals a powerful 10 damage to the monster!")

    def poisonAttack(self):
        """
        called when the user inputs '4' and chooses to poison the monster
        """
        # chooses a random number between 2 and 5, inclusive
        poisonAdd = random.randint(2, 5)
        # adds the random number to the amount of poison the monster receives
        self.poison += poisonAdd
        # prints the monster is poisoned and how much the current poison level is
        print(f"You poison the monster! Poison level: {self.poison}")


    def monsterAttack(self):
        """
        Runs the monster's turn. Called by playRound after the player
        acts, as long as the monster is still alive. The monster attacks,
        an active ally can block some damage, and then poison hurts the monster.
        """
        # generates a random number for damage from 2 to 6, inclusive
        damage = random.randint(2, 6)

        # runs if the user has recruited an ally
        if self.allyActive:
            # generates a random number to reduce the damage done by the monster by from
            # 1 to 3, inclusive
            reduction = random.randint(1, 3)
            # damage done by the monster is decreased by the amount of damage an ally blocked
            damage -= reduction
            # another edge case where the damage cannot go below 0, or the attack would heal the player
            if damage < 0:
                damage = 0
            # prints how much damage an ally blocked
            print(f"Your ally blocks some damage! Reduction: {reduction}")
            # an ally can only block damage once so once it does it is turned back off
            self.allyActive = False
        # subtracts the final damage from the players hp
        self.playerHp -= damage
        # prints out how much you got attacked for and your final hp after the attack
        print(f"The monster attacks you for {damage} damage! Your HP: {self.playerHp}")
        # if the monster is poisoned this if statement damages it after it attacks the user
        # bug noted: the monster's hp is not checked after this, so if the poison kills the
        # monster on the same turn the player dies, the game says the player still lost
        # *fix this if edits are made to the code*
        if self.poison > 0:
            # removes amount of poison from the monster's hp
            self.monsterHp -= self.poison
            # prints out how much damage the poison deals to the monster
            print(f"The poison deals {self.poison} damage to the monster!")
            # removes 1 from the poison total amount each round
            self.poison -= 1


def playRound(gameFile, roundNumber):
    """
    This function runs a single fight from start to finish, it returns win or loss so the
    main can track the overall record of the fight
    *this along with my class was added afterwards*
    """
    #this creates a new fight object so the constructor runs and stats reset each round
    fight = Fight()

    # prints the round number
    print(f"Round {roundNumber}")
    # prints at the start of every game
    print("A fierce Monster appears before you!")
    # prints your hp
    print(f"Your HP: {fight.playerHp}")
    # prints the monster's hp / out of max hp
    print(f"Monster HP: {fight.monsterHp}/{fight.monsterMaxHp}\n")

    # logs that this round started to the game file
    gameFile.write(f"Round {roundNumber} started\n")

    # this loop runs until a return ends it, each pass is one turn
    while True:
        # prints your hp / out of max hp
        print(f"Your HP: {fight.playerHp}/{fight.playerMaxHp}")
        # prints the monsters hp / out of max hp
        print(f"Monster HP: {fight.monsterHp}/{fight.monsterMaxHp}")

        # runs if poison done to monster is greater than 0
        if fight.poison > 0:
            # prints how much the monster is poisoned by
            print(f"Monster is poisoned! (Level {fight.poison})")
        # runs if the user has 1 or 2 allies
        if 0 < fight.allyCount < 3:
            # prints how many allies you have summoned
            print(f"Ally summoned {fight.allyCount} time(s)")
        # runs if the monster has between 1 and 9 hp
        if 0 < fight.monsterHp < 10:
            # prints the monster is almost dead
            print("The monster is almost dead!")
        # prints an empty line to keep my outputs clean
        print()
        # outputs different actions for the user to choose from
        print("Choose your action:")
        print("1 - Attack")
        print("2 - Heal")
        print("3 - Ally")
        print("4 - Poison")
        # prompts the user to input their chosen action
        choice = input("Enter your choice (1-4): ")
        print()

        # this was another edge case I had to fix
        # if the user did not input a valid choice this loop keeps running until they do
        while choice not in ("1", "2", "3", "4"):
            # prints that the user input an invalid choice and to try again
            print("Invalid choice, please enter a number from 1 to 4.")
            # accepts a new input from the user and overrides the old choice input
            choice = input("Enter your choice (1-4): ")
            # prints a new line after to keep my output nice and clean
            print()
        # runs if the user chose 1
        if choice == "1":
            # my code calls the attack method in the fight class
            fight.attack()
            # logs attack was chosen in the game file
            gameFile.write("Attack\n")
        # runs if the user chose 2
        elif choice == "2":
            # my code calls the heal method in the fight class
            fight.heal()
            # logs heal was chosen in the game file
            gameFile.write("Heal\n")
        # runs if the user chose 3
        elif choice == "3":
            # calls the ally method in the fight class
            fight.ally()
            # logs that ally was chosen in the game file
            gameFile.write("Ally\n")
        # runs if the user chose 4
        elif choice == "4":
            # calls the poison attack method in the fight class
            fight.poisonAttack()
            # logs that poison was chosen in the game file
            gameFile.write("Poison\n")
        # prints another empty line to keep the output clean for the user
        print()

        # runs if the monster's health goes below or equals 0
        if fight.monsterHp <= 0:
            # prints the monster is dead
            print("VICTORY! You have defeated the Monster!")
            # logs the player won and what round they won at in the game file
            gameFile.write(f"Round {roundNumber}: Player Won\n")
            # returns win back to the main function
            return "win"

        # calls the monster attack function in the fight class and this
        # handles all the outputs as well
        fight.monsterAttack()
        # new line is printed to keep the output clean
        print()

        # runs if the player's hp goes below or equal to 0
        if fight.playerHp <= 0:
            # prints they died to the monster
            print("DEFEAT! You have been defeated by the Monster...")
            # logs in the game file that the user lost and what round they lost on
            gameFile.write(f"Round {roundNumber}: Monster Won\n")
            # returns loss to the main function
            return "loss"


# Main function to run the game, including replay and the win/loss record
def main():
    # opens a file to log the game
    gameFile = open("gamelog.txt", "w")
    # welcomes the user to the game
    print("WELCOME TO MONSTER COMBAT!\n")

    # sets amount of wins to 0
    wins = 0
    # sets amount of losses to 0
    losses = 0
    # sets the round to the first round
    roundNumber = 1

    # sets playing to true
    playing = True
    # runs while the playing is set to true
    while playing:
        # accepts the output as result from the playRound function and sends 'gameFile' and 'roundNumber' to that function
        result = playRound(gameFile, roundNumber)
        # runs if the result is equal to win
        if result == "win":
            # adds 1 to the win counter
            wins += 1
        # this runs if the result does not equal win
        else:
            # adds a loss to the loss counter
            losses += 1
        # adds 1 to the round number
        roundNumber += 1
        # prints a blank line again
        print()
        # prints the users current record
        print(f"Record so far: {wins} wins, {losses} losses")
        # prints allowing the user to go again and sets the input to the 'again' variable
        # strip removes extra spaces from the start and end of the letter the user inputs
        # lower will lowercase the inputted letter
        again = input("Play another round? (y/n): ").strip().lower()
        # prints another blank line
        print()

        # if the user does not input y then the playing status is set to false
        if again != "y":
            playing = False
    # prints out the final record of wins and losses when playing is set to false
    print(f"Final record: {wins} wins, {losses} losses")
    # logs the final record to the game file
    gameFile.write(f"Final record: {wins} wins, {losses} losses\n")
    # closes the game file once the game is over and playing is set to false
    gameFile.close()

# starts my main :)
main()