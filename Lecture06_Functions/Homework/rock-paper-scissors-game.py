print("Welcome to the Rock Paper Scissors Game!")
player_1 = "Duo"
player_2 = "Mario"

def compare(item_1, item_2):
    if item_1 == item_2:
        return("It's a tie!")
    elif item_1 == 'rock':
        if item_2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif item_1 == 'scissors':
        if item_2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif item_1 == 'paper':
        if item_2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Uh, that's not valid! You have not entered rock, paper or scissors.")
    
player_1_choice = input("%s, rock, paper, or scissors?" % player_1)    
player_2_choice = input("%s, rock, paper, or scissors?" % player_2)    

print(compare(player_1_choice, player_2_choice))