import random


def play():
    user_choice = input(
        "Choose 'r' for Rock, 'p' for Paper or 's' for Scissors: ").lower()
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        user_choice = input(
            "It\'s a tie! You want to play again? (Y/N): ").lower()
        if user_choice == 'y':
            return play()
        else:
            return "Thank you for playing!"

    if is_win(user_choice, computer_choice):
        return f"You won! Computer choose {computer_choice}"

    return f"You lost! Computer choose {computer_choice}"


def is_win(player, opponent):
    if (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') \
            or (player == 'r' and opponent == 's'):
        return True


print(play())
