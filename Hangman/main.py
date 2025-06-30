
word = ('enter word here')

guessed_letters = []

guesses = 6
while True:

    player_letter = input('\nEnter a Letter\n')

    guessed_letters.append(player_letter)

    if player_letter not in word:
        guesses -= 1
        print('Wrong')

    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_',end=' ')
    print(f'\n{guesses} guesses left')

    won = True
    for letter in word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        print('\nYou win')
        break

    if guesses == 0:
        print('\nGame over\nThe word was', word)
        break
