import random


def play():
    user = input(f"Throw # {count}. Type 'r' for Rock, 'p' for Paper or 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        tie_count.append(1)
        return f"Tie. Computer chose {computer}"
    if user_win(user, computer):
        win_count.append(1)
        return f"You won! Computer chose {computer}"
    if user_lose(user, computer):
        lose_count.append(1)
        return f"You lost. Computer chose {computer}"
    if wrong(user):
        return "Your selection is invalid, try again"


def user_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (
            player == 's' and opponent == 'p'):
        return True


def user_lose(player, opponent):
    if (player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's') or (
            player == 's' and opponent == 'r'):
        return True


def wrong(player):
    if player != 'r' or player != 'p' or player != 's':
        return True


games = 5
print(f"Play Rock/Paper/Scissors with the Computer, best out of {games}")
count = 1
win_count = []
lose_count = []
tie_count = []

while count < games + 1:
    print(play())
    count += 1
    if count == games + 1:
        print("The game is over")
        break
print(f"Wins = {len(win_count)}, Loses = {len(lose_count)}, Ties = {len(tie_count)}")
