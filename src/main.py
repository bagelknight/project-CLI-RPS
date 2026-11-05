# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
import random
WINS = 0
LOSES = 0

while True:
    print("Welcome to rock paper")
    print("Main menu:")
    print("[1] play RPS")
    print("[2] Stats")
    print("[3] instructions")
    print("[4] Exit")

    play_choice = input("what would you like to do? ")
    if(play_choice == "1"):
        pass
    elif(play_choice == "2"):
        pass
    elif(play_choice == "3"):
        pass
    elif(play_choice == "4"):
        break
    else:
        play_choice = input("#WatDaMean try again ")

    def playRPS(shoot, compshot):
        
        