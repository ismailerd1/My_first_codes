import random
while True:
  choices = ['rock', 'paper', 'scissors']
  computer = random.choice(choices)
  player = input('rock paper or scissors? ').lower()


  while player not in choices:
    print("This is not a valid choice. Choose again!")
    player = input('rock paper or scissors? ')

  if player == 'rock':
    if computer == 'scissors':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('You won!')
    elif computer == 'paper':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('You lose!')
    elif computer == 'rock':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('Tie!')


  elif player == 'paper':
    if computer == 'scissors':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('You lose!')
    elif computer == 'paper':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('Tie!')
    elif computer == 'rock':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('You win!')


  elif player == 'scissors':
    if computer == 'scissors':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('Tie!')
    elif computer == 'paper':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('You win!')
    elif computer == 'rock':
      print("computer's choice:" + computer)
      print("player's choice:" + player)
      print('You lose!')

  play_again = input('Do you want a play again?(yes/no)').lower()
  if play_again != "yes":
    print('Thanks for playing!')
    break






