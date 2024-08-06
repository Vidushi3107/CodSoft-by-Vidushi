import random
class RockPaperScissor:
    def __init__(self):
        self.menu()

    def menu(self):

        user_input = input('''Enter your choice: 
                            1. Rock
                            2. Paper
                            3. Scissor 
                            ''')


        choices = ['rock', 'paper', 'scissor']
        computer_input = random.choice(choices)

        print("You choose", user_input)
        print("Computer choose ", computer_input)

        if user_input == computer_input:
            print("Both players selected same. It's a tie.")
        
        elif user_input == 'rock' and computer_input == 'scissor':
            print("Rock smashes scissors! You win!")
        
        elif user_input == 'paper' and computer_input == 'rock':
            print("Paper covers rock! You win!")
            
        elif user_input == 'scissor' and computer_input == 'paper':
            print("Scissors cuts paper! You win!")

        else:
            print("Computer Win!")

        new_game = input("Do you want to play again (yes/no): ")
        if new_game == 'yes':
            return self.menu()
        else:
            print("Game Over")

obj = RockPaperScissor()
