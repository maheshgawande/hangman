import random

def get_word():
    txt_file = open('hangman/words_list.txt', 'r')
    file_data = txt_file.read().split('\n')
    words_list = []
    for word in file_data:
        if len(word) > 4 and len(word) <= 6:
            words_list.append(word)

    words_list = tuple(words_list)
    word = random.choice(words_list)
    return word


def hangman():
    actual_word = get_word()
    print(len(actual_word), ' letter word')
    guessed_word = ['-' for each_letter in actual_word]

    chances = 4
    not_hanged = True
    not_winner = True
    while not_hanged and not_winner:
        dashed_line = ''
        dash_count = 0
        for i in guessed_word:
            dashed_line += i
            if i == '-':
                dash_count += 1

        print('Chances: ', chances)
        print(dashed_line)

        change_count = 0
        if dash_count > 0:
            while True:
                current_letter = input('> ')
                if current_letter != '':
                    try:
                        type(int(current_letter))
                        print(f"{current_letter} is not a character/letter!")
                    except ValueError:
                        break
                else:
                    print("Please do not leave input empty!")

            for i in range(len(actual_word)):
                if actual_word[i] == current_letter:
                    guessed_word[i] = current_letter
                    change_count += 1
        else:
            not_winner = False

        if change_count < 1 and not_winner:
            chances -= 1
            if chances == 0:
                not_hanged = False

    if not_winner:
        print('\nLooser, you just hanged the man!\nThe word was:', actual_word)
        print('__________')
        print('|    |')
        print('|    O')
        print('|   / \\')
        print('|    |')
        print('|   / \\')
    else:
        print('\nHooray, you just saved the man!\nThe word is:', actual_word)


hangman()