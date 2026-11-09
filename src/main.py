# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.
from game import playRPS
from stats import record_result, show_stats

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
                result = playRPS()
                record_result(result)
                again = input("play again? yes or no ")
                if again != "yes":
                    break
        elif(play_choice == "2"):
            show_stats()
        elif(play_choice == "3"):
            break
        else:
            print("#WatDaMean try again")

main()
        