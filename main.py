import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns,lines, bet,values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings +=values[symbol]*bet
            winning_lines.append(line + 1)
    return winnings,winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol ,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns = []
    for _ in range(cols):
        column = []
        current_symbols= all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) 
            column.append(value)
            
        columns.append(column)
    return columns
        
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:    
                print(column[row], end=" ")
        print()
         




def deposit():
    while True:     
        amt = input("what amount would you like to deposit?  $")
        if amt.isdigit() :
            amt = int(amt)
            if amt > 0 :
                break
            else :
                print("Amount should be grater than 0.")
        else:
            print("Invalid Amount.")
    return amt


def get_number_of_lines():
    while True:     
        NumOfLine = input("Enter the numbers of lines to bet on (1-" + str(MAX_LINES) + ") ? ")
        if NumOfLine.isdigit() :
            NumOfLine = int(NumOfLine)
            if 1<= NumOfLine <= MAX_LINES:
                break
            else :
                print("Enter valid number of lines.")
        else:
            print("Please enter a valid Amount.")
    return NumOfLine
    

def get_bid():
    while True:     
        amt = input("How much amount would you like to bet ?  $")
        if amt.isdigit() :
            amt = int(amt)
            if MIN_BET <= amt <= MAX_BET :
                break
            else :
                print(f"Amount must be between ${MIN_BET} - {MAX_BET}")
        else:
            print("Invalid Amount.")
    return amt


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bid()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"Insufficient balance. You total bet is ${total_bet} but your Balance is ${balance}")
        else:
            break
        
        
    print(f"Your betting ${bet} on {lines}. Total bet is equal to: ${total_bet}." )
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        responce = input("press enter to play (q to quit)")
        if responce == "q":
            break
        balance+=spin(balance)
        
    print(f"you left with ${balance} ")
    
    
    
    
    
main()
    