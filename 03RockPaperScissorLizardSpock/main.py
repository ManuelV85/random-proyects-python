import random

def play(): 
    user = input("What\'s your choise? 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizard, 'k' for spock: ")
    computer = random.choice(['r', 'p', 's','l','k'])

    if user == computer:
        return 'it\'s tie'
    
    #remember s>p, p>r, r>l, l>k, k>s, s>l, l>p, p>k, k>r, r>s
    if is_win(user, computer):
        return "You won!!"

    return "You lost.!!! T.T"

def is_win(player, opponet):

    if (player == 's' and opponet=='p') or (player == 'p' and opponet=='r') or (player == 'r' and opponet=='l') or (player == 'l' and opponet=='k') \
    or (player == 'k' and opponet=='s') or (player == 's' and opponet=='l') or (player == 'l' and opponet=='p') or (player == 'p' and opponet=='k') \
    or (player == 'k' and opponet=='r') or (player == 'r' and opponet=='s'):
        return True
    
print(play())