import random

def rock_paper_scissors():
    num_rounds = int(input("Enter the number of rounds you want to play: "))
    user_score = 0
    computer_score = 0

    for round_num in range(1, num_rounds + 1):
        print("\nRound", round_num)
        print("1 - Rock\n2 - Paper\n3 - Scissor")

        random_number = random.randint(1, 3)
        user_turn = int(input("Your Turn: "))

        if 1 <= user_turn <= 3:
            print("Computer Turn:", random_number)

            if (random_number == 1 and user_turn == 1) or (random_number == 2 and user_turn == 2) or (random_number == 3 and user_turn == 3):
                print("Match Is Draw!")
            elif (random_number == 1 and user_turn == 2) or (random_number == 2 and user_turn == 3) or (random_number == 3 and user_turn == 1):
                print("Congratulations, You Win!")
                user_score += 1
            elif (random_number == 1 and user_turn == 3) or (random_number == 2 and user_turn == 1) or (random_number == 3 and user_turn == 2):
                print("You Lose!")
                computer_score += 1
        else:
            print("Enter a valid choice (1, 2, or 3)!")
            round_num -= 1

    print("\nGame Over!")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    if user_score > computer_score:
        print("Congratulations, You Win the Game!")
    elif user_score < computer_score:
        print("Computer Wins the Game!")
    else:
        print("The Game is a Draw!")


print("Welcome to Rock, Paper, Scissors Game!")
rock_paper_scissors()
