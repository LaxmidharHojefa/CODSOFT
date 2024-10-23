import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    """Prompt the user to input rock, paper, or scissors."""
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the rules of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the result of the current round."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_again():
    """Ask the user if they want to play another round."""
    while True:
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay in ["yes", "no"]:
            return replay == "yes"
        else:
            print("Please enter 'yes' or 'no'.")

def rock_paper_scissors_game():
    """Main function to play the rock, paper, scissors game."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Display current scores
        print(f"\nCurrent Scores - You: {user_score}, Computer: {computer_score}")

        # Check if the user wants to play again
        if not play_again():
            break

    # Final scores
    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thank you for playing!")

if __name__ == "__main__":
    rock_paper_scissors_game()

