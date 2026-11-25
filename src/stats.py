WINS = 0
LOSES = 0

def record_result(result):
    global WINS, LOSES
    if result == "win":
        WINS += 1
    elif result == "loss":
        LOSES += 1

def show_stats():
    total = WINS + LOSES
    print(f"you have {WINS} wins and {LOSES} losses")
    if total > 0:
        print(f"your current win rate is {WINS / total * 100:.0f}%")
    else:
        print("your win rate is 0 percent")