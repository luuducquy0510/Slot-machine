import random

MAX_COLS = 3
MAX_ROWS = 3

icons_dic = {
    'A' : 2,
    'B' : 4,
    'C' : 8,
    'D' : 10,
    }  # The more value the less it has

icons_value = {
    'A' : 10,
    'B' : 5,
    'C' : 3,
    'D' : 2,
    }   # Value of each icon

def deposit():
    while True:
        deposit = input('Please input the amount you want to deposit: $')
        if deposit.isdigit():
            print(f'Your balance is ${deposit}')
            break
        else:
            print('The input is invalid, please input again $')
    return int(deposit)

def get_line():
    while True:
       line = input('How many lines do you want to bet on? ')
       if line.isdigit() and int(line) <= MAX_ROWS:
           print(f'You bet in {line} lines')
           break
       else:
           print('The input is invalid, please input again')
    return int(line)

def get_line_bet():
    while True:
       line_bet = input('How much do you want to bet on each line? $') #Line from top to bottom
       if line_bet.isdigit():
           print(f'You bet ${line_bet} on each line')
           break
       else:
           print('Please input again: $')
    return int(line_bet)
           
        
'''-----------------------slot machine create-------------------------'''
        
def get_slot_machine(rows, cols, icons):
    total_icons = []
    for icon, icon_counts in icons.items():
        for _ in range(icon_counts):
            total_icons.append(icon)
    
    machine = []
    for _ in range(cols):
        columns = []
        for _ in range(rows):
            current_icons = total_icons[:] #Make a copy if icon list to remove icon after pick
            icon = random.choice(current_icons)
            current_icons.remove(icon)
            columns.append(icon)
        
        machine.append(columns)
    return machine
      
def print_slot_machine(machine): #Change each list in a nested list into a column
    for row in range(len(machine[0])):
        for i, columns in enumerate(machine):
            if i != int(len(machine)-1):
                print(columns[row], '|', end = ' ')
            else:
                print(columns[row], end = '\n')
                
def check_win(nested_list, lines, bet, values):
    winning = 0
    for line in range(lines):
        icon = nested_list[0][line]
        for column in nested_list:
            check_icon = column[line]
            if icon != check_icon:
                break
        else:
            winning += values[icon] * bet
    return winning  
    
    
'''---------------------------Game running------------------------'''
balance = deposit()

def main():
    global balance
    while True:
        rows = get_line() 
        row_value = get_line_bet()
        total_bet = int(rows)* int(row_value)
        if total_bet <= int(balance):
            print(f'You bet ${total_bet} in total')
            balance -= total_bet
        else:
            print('Your balance is not enough to bet')
            break
        
        machine = get_slot_machine(MAX_ROWS, MAX_COLS, icons_dic)   
        slot_machine = print_slot_machine(machine)
        win_money = check_win(machine, rows, row_value, icons_value)
        if win_money > 0:
            print(f'You win ${win_money}')
            balance += win_money
            print(f'Do you want to keep playing with ${balance}')
        else:
            print('You win $0')
            print(f'Do you want to keep playing with ${balance}')
        break

def play_game():
    while True:
        if balance > 0: 
            answer = int(input('Press 1 to play the game, 0 to quit the game: '))
            if answer == 1:
                main()
            elif answer == 0:
                print(f'You leave with ${balance}. Thank you for playing the game.')
                break
            else:
                print('Please answer again')
        else:
            print('You have no money left to play. Thank you for playing the game!')
            break
play_game()     