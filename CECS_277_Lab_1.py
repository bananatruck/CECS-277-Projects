# Keshav Jindal
# CECS 277
# Lab 1 - Python Basics

import check_input
import random

def cup_game_():
    money = 100
    
    while money > 0:
        print(f"\nYou currently have ${money}")
        
        # Place the ball under one of the cups randomly
        ball_position = random.randint(1, 3)
        bet_amount = check_input.get_int_range("Bet amount? ", 1, money)
        
        # Get user input guess
        
        print('  ___     ___     ___ ')
        print(' /   \\   /   \\   /   \\')
        print('/  1  \\ /  2  \\ /  3  \\')
        print('------- ------- -------')
        user_input = int(input("Guess the location of the ball (1-3): "))
    
        if 1 <= user_input <= 3:
            if ball_position == 1:
                print('  ___     ___     ___ ')
                print(' /   \\   /   \\   /   \\')
                print('/  o  \\ /     \\ /     \\')
                print('------- ------- -------')

            elif ball_position == 2:
                print('  ___     ___     ___ ')
                print(' /   \\   /   \\   /   \\')
                print('/     \\ /  o  \\ /     \\')
                print('------- ------- -------')

            elif ball_position == 3:
                print('  ___     ___     ___ ')
                print(' /   \\   /   \\   /   \\')
                print('/     \\ /     \\ /  o  \\')
                print('------- ------- -------')
 
        else:
            print("Invalid guess. Please enter a number between 1 and 3. ")

        # Check the validity of a guess
        if guess == ball_position:
            money += bet_amount
            print(f"Congratulations! The ball was under shell {ball_position}. You won ${2 * bet_amount}.")
        else:
            money -= bet_amount
            print(f"Sorry, the ball was under shell {ball_position}. You lost ${bet_amount}.")

            if money == 0:
                break

            
        play_again = check_input.get_yes_no("Do you want to play again? (Y/N): ")

        if play_again != 'y':
            pass
        else:
            print("Thank you for playing!")
            break

    print("You are out of money! Game over.")

if __name__ == "__main__":
    cup_game_()
