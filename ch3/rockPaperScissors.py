import random

winner = '' # set up winner variable as empty string
random_choice = random.randint(0,2) # computer randomly chooses number between 0 & 2

# Way Two to write the code
# choices = [ 'rock', 'paper', 'scissors']
# computer_choice = random.choices(choices)

#Option One to Write the code program - does the same as option Two
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'
# Above code uses random number to then attach 1.rock 2.paper 3.scissors to random number
# print('The computer chooses', computer_choice)

user_choice = ''
while (user_choice != 'rock' and 
       user_choice != 'paper' and
       user_choice != 'scissors'):
    user_choice = input('Please enter choice of either rock paper or scissors? ')

# print('You chose',user_choice, 'and the computer chooses', computer_choice)

if user_choice == computer_choice:
    winner = 'Tie'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
else:
    winner = 'User'
# Above if else statement is the game logic to define whether computer or user wins
if winner == 'Tie':
    print( 'We both chose', computer_choice + ', play again.')
else:
    print('You chose',user_choice, 'and the computer chose', computer_choice, 'the winner is', winner)






