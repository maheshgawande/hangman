txt_file = open('hangman/raw_words_list.txt')
words_list = txt_file.read().split('\n')

new_file = open('hangman/sorted_word_list.txt', 'w')
for word in words_list:
    if len(word) > 4 and len(word) <= 6:
        new_file.write(f"{word}\n")