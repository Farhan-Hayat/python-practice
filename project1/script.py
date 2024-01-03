import random
def computer_func():
  computer = random.choice(['r','p','s'])
  return computer

def user_func():
  user=input("Enter your choice (r/p/s): ")
  return user


def game():
  exit = 'n'
  while(exit == 'n'):
    users_choice = user_func()
    computers_choice = computer_func()
    if((users_choice == 'r' and computers_choice == 's') or (users_choice == 's' and computers_choice == 'p') or (users_choice == 'p' and computers_choice == 'r')):
      print("You won")
    
    else:
      print("you lost")
    exit = input("Do you wnat to exit (y/n) : ")

game()




