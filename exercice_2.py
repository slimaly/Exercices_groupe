import random

def game_on(number, random_num):
    number_of_tries = 0
    
    while True:
        user_input = input("Enter a number to guess the right one: ")
        
        if not user_input:
            break
        
        user_input = int(user_input)
        
        if 1 <= user_input <= 100:
            number_of_tries += 1
            
            if user_input == random_num:
                return f"Bravo! You've won the game. It took you {number_of_tries} tries to win."
            elif user_input < random_num:
                print(f"Sorry, the number's too small! Try again! This is your {number_of_tries} attempt.")
            else:
                print(f"Sorry, the number's too large! Try again! This is your {number_of_tries} attempt.")
        else:
            return "Error: Number submitted must be between 1 and 100"


def game_mode():
    player = 1
    Warrior = player
    Clan = player + 1
    
    user == Warrior or Clan
    
    while True:
        user_input_mode == input("Choose mode: {Warrior}/{Clan}")
        
        if user == Clan:
            Clan.append
            
        else:
            return Warrior
            
        
    
   

def Easy():   
    print("You have chosen Easy.You are only allowed to choose any number between 1 - 30")
    number_range = (1, 30)
    random_num = random.randint(*number_range)
    return game_on(number_range, random_num)
     
def Intermediate():
    print("You have chosen Intermediate.You are only allowed to choose any number between 1-60")
    number_range = (1, 60)
    random_num = random.randint(*number_range)
    return game_on(number_range, random_num)
     
def Difficult(): 
    print("You have chosen Difficult.You are only allowed to choose any number between 1 - 100")
    number_range = (1, 100)
    random_num = random.randint(*number_range)
    return game_on(number_range, random_num)  


choose_game_mode = input ("Choose mode: (Warrior or Clan)")
if choose_game_mode in ["Warrior", "Clan"]:
    result = globals()[choose_game_mode]()
    print(result)
else:
    print("Invalid entry. Please choose among the provided options.")

choose_difficulty = input("Choose the difficulty you wish: (Difficult, Intermediate, Easy)")

if choose_difficulty in ["Easy", "Intermediate", "Difficult"]:
    result = globals()[choose_difficulty]()
    print(result)
else:
    print("Invalid entry. Please choose among the provided options.")