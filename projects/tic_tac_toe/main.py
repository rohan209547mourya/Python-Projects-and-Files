row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
user1_choice = ''
user2_choice = ''
isPlaying = True  # if True then player1 is playing else player 2 is playing

print('________________________________________________________')
print(' Welcome, this is a multiplayer TIC-TAC-TOE Game🎉🎉✨')
print('________________________________________________________')

print('\n\n')


def show_board():
    print('      |         |        ')
    print(f'{row1[0]}     |  {row1[1]}      | {row1[2]}      ')
    print('      |         |        ')
    print('_________________________')
    print('      |         |        ')
    print(f'{row2[0]}     |  {row2[1]}      | {row2[2]}      ')
    print('      |         |        ')
    print('_________________________')
    print('      |         |        ')
    print(f'{row3[0]}     |  {row3[1]}      | {row3[2]}      ')
    print('      |         |        ')


def input_user_choice():
    global user1_choice
    global user2_choice
    user1_choice = input('Pick your choice (X or O) : ')
    user1_choice = user1_choice.upper()

    if user1_choice != 'X' and user1_choice != 'O':
        if user1_choice.isdigit():
            print(f'Invalid user input {user1_choice} ❌')
            input_user_choice()
        print(f'Invalid user input {user1_choice} ❌')
        input_user_choice()

    if user1_choice == 'X':
        user2_choice = 'O'
    else:
        user2_choice = 'X'


def fill_game_board():
    global isPlaying
    column_number = input('Input a number between 1 to 9 \nNOTE: 1 and 9 represent 1st and 9th column respectively \n '
                          ': ')

    if not column_number.isdigit():
        print('Invalid type of input, expected a number ❌')
        fill_game_board()

    column_number = int(column_number)
    if 3 >= column_number >= 1:
        fill_row_helper(row=row1, column=column_number-1, player=isPlaying)

    elif 6 >= column_number >= 4:
        fill_row_helper(row=row2, column=column_number-4, player=isPlaying)

    elif 9 >= column_number >= 7:
        fill_row_helper(row=row3, column=column_number-7, player=isPlaying)

    else:
        print('Invalid range of input, should be 1 to 9 ❌')
        fill_game_board()


def fill_row_helper(row: list, column: int, player: bool):
    global isPlaying, user1_choice, user2_choice

    if row[column] == 'X' or row[column] == 'O':
        print('you can\'t choose this column ❌')
        fill_game_board()

    if player:
        row[column] = user1_choice
    else:
        row[column] = user2_choice

    isPlaying = not isPlaying
    show_board()
    fill_game_board()


def validate_board():
    pass


input_user_choice()
show_board()
fill_game_board()
