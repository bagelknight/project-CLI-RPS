import random

def playRPS():
    choice = input("rock, paper, or scissors? ")
    while choice != "rock" and choice != "paper" and choice != "scissors":
        choice = input("dude rock paper or scissors? ")

    cpuPick = random.randint(1, 3)
    if(cpuPick == 1):
        cpuPick = "rock"
    elif(cpuPick == 2):
        cpuPick = "paper"
    else:
        cpuPick = "scissors"

    print(f"cpu picked {cpuPick}")

    if(choice == cpuPick):
        print("tie??")
        result = "tie"
    elif(choice == "rock" and cpuPick == "scissors") or (choice == "paper" and cpuPick == "rock") or (choice == "scissors" and cpuPick == "paper"):
        print("you wins!")
        result = "win"
    else:
        print("cpu wins?")
        result = "loss"

    return result