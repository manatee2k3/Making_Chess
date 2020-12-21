## Hangman ##
import random


man = {'head': ' ', 'torso': ' ', 'L-arm': ' ', 'R-arm': ' ', 'L-leg': ' ', 'R-leg': ' '} 

def hangman_board(man):
    print('____________________')
    print()
    print('  |--| ')
    print('  |/ '+ (man)['head'] + ' ')
    print('  | ' + (man)['R-arm'] + (man)['torso'] + (man)['L-arm'])
    print('--| ' + (man)['R-leg' ]+ ' ' + (man)['L-leg'])
    print()
          
def get_index_positions(list_of_elements, elements):
    index_list = []
    index_num = 0
    while True:
        try:
            index_num = list_of_elements.index(elements, index_num)
            index_list.append(index_num)
            index_num += 1
        except ValueError as e:
            break
    return index_list



word_list = []

with open('Christmas List.txt', 'r') as f:
    sowpods = f.read()
    sowpods = sowpods.upper()
for line in sowpods.splitlines():
    word_list.append(str(line))

r = random.randint(1,len(word_list))

word = word_list[r]

word_string = []
for character in word:
    word_string.append(str(character))

covered = ['_']*len(word)

word_set = set(word)


print('Welcome to Hangman.')
log_guesses = []
x = 0

while x <= 5:
    hangman_board(man)
    print(*log_guesses, sep =" ")
    print()
    print(*covered, sep=" ")
    print()
    guess = input('your guess: ')
    guess = guess.upper()
    if guess not in log_guesses:
        if guess in word_set:
            index_list = get_index_positions(word_string, guess)
            for i in index_list:
                 covered[i] = guess
                 if '_ ' in covered:
                     print('Congrats! you have guessed the right answer! ')
        else:
            print("That letter's not in the word")
            x += 1
            if x == 1:
                man['head'] = 'O'
            elif x == 2:
                man['torso'] = '|'
            elif x == 3:
                man['L-arm'] = "\\"
            elif x == 4:
                man['R-arm'] = '/'
            elif x == 5:
                man['L-leg'] = '\\'
            elif x == 6:
                man['R-leg'] = '/'
                hangman_board(man)
                print(*word_string, sep=" ")
                print('GAME OVER.')
                break 

    else:
        print('You have already guessed ' + guess + '. Perhaps try another letter.')
    log_guesses.append(guess)
