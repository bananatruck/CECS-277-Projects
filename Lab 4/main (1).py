from player import Player 
from check_input import get_yes_no

def take_turn(player):
    """
    Simulates taking a turn in Yahtzee.
    Rolls the dice, checks for any winning conditions, and updates the score.

    Args:
        player (Player): The player taking the turn.
    """
    player.roll_dice()
    print(player) # Display the dice values after rolling.
    win_types = []
    if player.has_pair():
        win_types.append('a pair!')
    if player.has_three_of_a_kind():
        win_types.append('3 of a kind!')
    if player.has_series():
        win_types.append('a series of 3!')

    if win_types:
        print(f"You got {', and '.join(win_types)}!")
    else:
        print("Aww. Too bad.")

    print(f"Score = {player.get_points()}")

def main():
    """
    The main function to run the game of Yahtzee.
    Creates a player and allows them to take turns until they choose to stop.
    """
    player =Player ()

    while True:
        take_turn(player) # Player takes a turn

        # Check if the player wants to play again
        if not get_yes_no("Play again? (Y/N): "):
            break # Exit the loop if the player chooses not to continue
        print()
print()
print("Game Over.")
print(f"Final Score = {player.get_points()}")

if name == "_main_":
    print("-Yahtzee-")
main()