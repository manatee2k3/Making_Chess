chess = {'8a': 'bRk', '8b': 'bKn', '8c': 'bBi', '8d': 'bQI', '8e': 'bKI', '8f': 'bBi', '8g': 'bKn', '8h': 'bRk',
         '7a': 'bPa', '7b': 'bPa', '7c': 'bPa', '7d': 'bPa', '7e': 'bPa', '7f': 'bPa', '7g': 'bPa', '7h': 'bPa',
         '6a': '   ', '6b': '   ', '6c': '   ', '6d': '   ', '6e': '   ', '6f': '   ', '6g': '   ', '6h': '   ',
         '5a': '   ', '5b': '   ', '5c': '   ', '5d': '   ', '5e': '   ', '5f': '   ', '5g': '   ', '5h': '   ',
         '4a': '   ', '4b': '   ', '4c': '   ', '4d': '   ', '4e': '   ', '4f': '   ', '4g': '   ', '4h': '   ',
         '3a': '   ', '3b': '   ', '3c': '   ', '3d': '   ', '3e': '   ', '3f': '   ', '3g': '   ', '3h': '   ',
         '2a': 'wPa', '2b': 'wPa', '2c': 'wPa', '2d': 'wPa', '2e': 'wPa', '2f': 'wPa', '2g': 'wPa', '2h': 'wPa',
         '1a': 'wRk', '1b': 'wKn', '1c': 'wBi', '1d': 'wQU', '1e': 'wKI', '1f': 'wBi', '1g': 'wKn', '1h': 'wRk'}
#above is the dictionary that has all slots on the chess board.
#the chess pieces have been placed in the dictionary, correlating to their positon on the board 


def print_board(b):
    print('8 ' + b['8a'] + ' | ' + b['8b'] + ' | ' + b['8c'] + ' | ' + b['8d'] + ' | ' + b['8e'] + ' | ' + b['8f'] + ' | ' + b['8g'] + ' | ' + b['8h'])
    print('|-----------------------------------------------|')
    print('7 ' + b['7a'] + ' | ' + b['7b'] + ' | ' + b['7c'] + ' | ' + b['7d'] + ' | ' + b['7e'] + ' | ' + b['7f'] + ' | ' + b['7g'] + ' | ' + b['7h'])
    print('|-----------------------------------------------|')
    print('6 ' + b['6a'] + ' | ' + b['6b'] + ' | ' + b['6c'] + ' | ' + b['6d'] + ' | ' + b['6e'] + ' | ' + b['6f'] + ' | ' + b['6g'] + ' | ' + b['6h'])
    print('|-----------------------------------------------|')
    print('5 ' + b['5a'] + ' | ' + b['5b'] + ' | ' + b['5c'] + ' | ' + b['5d'] + ' | ' + b['5e'] + ' | ' + b['5f'] + ' | ' + b['5g'] + ' | ' + b['5h'])
    print('|-----------------------------------------------|')
    print('4 ' + b['4a'] + ' | ' + b['4b'] + ' | ' + b['4c'] + ' | ' + b['4d'] + ' | ' + b['4e'] + ' | ' + b['4f'] + ' | ' + b['4g'] + ' | ' + b['4h'])
    print('|-----------------------------------------------|')
    print('3 ' + b['3a'] + ' | ' + b['3b'] + ' | ' + b['3c'] + ' | ' + b['3d'] + ' | ' + b['3e'] + ' | ' + b['3f'] + ' | ' + b['3g'] + ' | ' + b['3h'])
    print('|-----------------------------------------------|')
    print('2 ' + b['2a'] + ' | ' + b['2b'] + ' | ' + b['2c'] + ' | ' + b['2d'] + ' | ' + b['2e'] + ' | ' + b['2f'] + ' | ' + b['2g'] + ' | ' + b['2h'])
    print('|-----------------------------------------------|')
    print('1 ' + b['1a'] + ' | ' + b['1b'] + ' | ' + b['1c'] + ' | ' + b['1d'] + ' | ' + b['1e'] + ' | ' + b['1f'] + ' | ' + b['1g'] + ' | ' + b['1h'])
    print('|-----------------------------------------------|')
    print('   A     B     C     D     E     F     G     H')

#printing the entire chess board 

turn = 'Player 1' #making a turn order, the rest of the code is below for this

for i in range(100): #limiting the loop to 100 turns 
    print_board(chess) #printing the board
    print ('Turn for ' + turn + '. What piece do you want to move?')
    print('write its location (e.g. 4a)')
    space = input() #finding out which space they want to move
    print('where do you want to move it?, write its location (e.g. 4a)')
    move = input() #where new chess piece will be placed                           
        
    chess[move] = chess[space] #moving the value in one key and placing it into the new position
    chess[space] = '   ' #adding blank spaces in the now empty key, so the board stays formatted 
        
    if turn == 'Player 1': #continuing the turn order 
        turn = 'Player 2' 
    else:
        turn = 'Player 1'



