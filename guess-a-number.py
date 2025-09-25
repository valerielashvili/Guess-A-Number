import random

computer_number = random.randint(1, 100)
tries = 0
restart_game = ''

while restart_game != 'no':
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)
    tries += 1

    if tries <= 6:
        if player_number == computer_number:
            print("You guess it!")
            break
        elif player_number > computer_number:
            print("Too high!")
        else:
            print("Too low!")
    else:
        print(f"Game over! You have used all your chances...\n")
        restart_game = input("Type [yes] to Play Again or [no] to quit: ")

        if restart_game == 'yes':
            continue
        else:
            print("Thank you for playing!")
            break