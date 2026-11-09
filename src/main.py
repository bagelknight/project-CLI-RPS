# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
import random
WINS = 0
LOSES = 0

def main():
    while True:
        print("Welcome to rock paper") 
        print("Main menu:")
        print("[1] play RPS")
        print("[2] Stats")
        print("[3] Exit")

        play_choice = input("what would you like to do? ")
        if(play_choice == "1"):
            while True:
                playRPS()
                again = input("play again? yes or no ")
                if again != "yes":
                    break
        elif(play_choice == "2"):
            print(f"you have a {WINS} wins and {LOSES}")
            if(WINS > 0):
                print(f"your current win rate is {WINS / LOSES}")
            else:
                print("your win rate is 0 percent")
        elif(play_choice == "3"):
            break
        else:
            play_choice = input("#WatDaMean try again ")

def playRPS():
    global WINS 
    global LOSES

    choice = input("rock, paper, or scissors? ")
    if(choice == "rock"):
        shoot = "rock"
        return shoot
    elif(choice == "paper"):
        shoot = "paper"
        return shoot
    elif(choice == "scissors"):
        shoot = "scissors"
        return shoot
    else:
        choice = input("dude rock paper or scissors? ")
        
    cpuPick = random.randint(1, 3)
    if(cpuPick == 1):
        cpuPick = "rock"
    elif(cpuPick == 2):
        cpuPick = "paper"
    elif(cpuPick == 3):
        cpuPick = "scissors"

    if(choice == cpuPick):
        print("tie??")
    if(choice == "rock" and cpuPick == "scissors"):
        print("you wins!")
        WINS +=1
    elif(choice == "rock" and cpuPick == "paper"):
        print("cpu wins?")
        LOSES +=1
    if(choice == "paper" and cpuPick == "scissors"):
        print("cpu wins?")
        LOSES +=1
    elif(choice == "paper" and cpuPick == "rock"):
        print("you wins!")
        WINS +=1
    if(choice == "scissors" and cpuPick == "rock"):
        print("cpu wins?")
        LOSES +=1
    elif(choice == "scissors" and cpuPick == "paper"):
        print("you win!")
        WINS +=1
    again = input("play again? yes or no ")
    if(again == "yes"):
        playRPS()
    else:
        main()        
main()
        