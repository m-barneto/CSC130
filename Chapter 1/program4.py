def is_valid(choice):
    return choice == "r" or choice == "p" or choice == "s"


def play():
    choice1 = input("Player 1: Enter R for rock, P for paper or S for scissors: ").lower()
    if not is_valid(choice1):
        return -1
    choice2 = input("Player 2: Enter R for rock, P for paper or S for scissors: ").lower()
    if not is_valid(choice2):
        return -1

    if choice1 == choice2:
        return 3

    if choice1 == "r" and choice2 == "s":
        return 1
    elif choice1 == "r" and choice2 == "p":
        return 2

    if choice1 == "p" and choice2 == "r":
        return 1
    elif choice1 == "p" and choice2 == "s":
        return 2

    if choice1 == "s" and choice2 == "p":
        return 1
    elif choice1 == "s" and choice2 == "r":
        return 2


result = play()
if result == 1:
    print("Player 1 has won the game.")
elif result == 2:
    print("Player 2 has won the game.")
elif result == 3:
    print("Tie")
else:
    print("Game canceled because of invalid entry.")
