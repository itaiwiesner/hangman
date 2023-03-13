def home_screen():
    """
    the function prints the home screen of the game and the max mistakes the suer can make
    :return: None
    """
    print("""Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")
    print(6)
    return None


def dict_hangman():
    """
    creates a dictionary.
    each key represents a number of tries.
    each value represents the hangman situation.
    returns the dictionary
    """
    HANGMAN_PHOTOS = {0: "x-------x",
                      1: """x-------x
|
|
|
|
|""",
                      2: """x-------x
|       |
|       0
|
|
|""",
                      3: """x-------x
|       |
|       0
|       |
|
|""",
                      4: """x-------x
|       |
|       0
|      /|\ 
|
|""",
                      5: """x-------x
|       |
|       0
|      /|\ 
|      /
|""",
                      6: """x-------x
|       |
|       0
|      /|\ 
|      / \ 
|"""}
    return HANGMAN_PHOTOS


def check_win(secret_word, old_letters_guessed):
    """
    the function gets the word the user has to guess, and a list of the letters the user has already guessed.
    the function checks if the user has won the game, if he guessed every letter correctly
    :param secret_word: the word the user has to guess
    :param old_letters_guessed: all of the user previous guesses
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if the user won, i.e. guessed all of the letters. else, False
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    the function gets a string and a list.
    the string represents the word the user has to guess.
    the list represents the letters the user has already guessed.
    the function returns a string which contains letters and under lines
    the letters are the letters that were guessed correctly, and appear in their right index.
    the under lines represent the letters which weren't guessed correctly yet.
    :param secret_word: the word the user has to guess
    :param old_letters_guessed: the letters the user has already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: a string of letters and under lines. the under lines are the indexes which haven't been guessed yet
    :rtype: str
    """
    output = ['_ '] * len(secret_word)
    for letter in old_letters_guessed:
        for index in range(len(secret_word)):
            if letter == secret_word[index]:
                output[index] = letter
    output = ' '.join(output)
    return output


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    the function gets a string and a list,
    checks if the string is an English letter (contains only 1 char, no matter if low or cap letter)
    and doesn't already appear in the list
    :param letter_guessed: user's guess
    :param old_letters_guessed: all user's previous guesses
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the string is an English letter, else, returns False
    :rtype: bool
    """
    # Check if the string contains 1 char
    if len(letter_guessed) > 1:
        return False
    # Check if the string is an English letter and Check if the letter was already guessed
    ascii_value = ord(letter_guessed)
    if (65 <= ascii_value <= 90 or 97 <= ascii_value <= 122) \
            and old_letters_guessed.count(letter_guessed) == 0:
        return True
    return False


# exe-6.4.2
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    the function gets a string and
    :param letter_guessed: the recent valid guess
    :param old_letters_guessed: a list contains all user's previous guesses
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: if the input is valid, returns True and adds the guessed letter to the end of the list
    if input is invalid, returns False, print 'X' and under the 'X', prints the list as a string of lowercase letters,
    sorted by value from low to high, and divided by '<-'
    :rtype: bool
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        msg_to_print = old_letters_guessed
        msg_to_print = ' '.join(msg_to_print).lower().split()
        msg_to_print.sort()
        msg_to_print = " -> ".join(msg_to_print)
        print(msg_to_print)
        return False

    old_letters_guessed.append(letter_guessed)
    return True


def choose_word(file_path, index):
    """
    gets a path to a text file of words and an index. returns the word in the given
    :param file_path: text file of words. the words are divided by space bar.
    :type file_path: str
    :param index: an index of a certain word in the file
    :return: the word in the index received
    :rtype: str
    """
    with open(file_path, 'r') as words_file:
        # getting the word in the index received
        words_list = words_file.read().split(' ')
        word_num = len(words_list)
        if index > word_num:
            index_in_list = index // word_num
            index = index - word_num * index_in_list
        return words_list[index - 1]


def main():
    path = 'words.txt'
    index = int(input(f'enter the index of a word from "{path}": '))
    secret_word = choose_word(path, index)
    MAX_TRIES = 6
    num_of_tries = 0
    old_letter_guessed = []
    HANGMAN_PHOTO = dict_hangman()

    # print the home screen
    home_screen()
    print("Let's play Hangman!")
    print(HANGMAN_PHOTO[num_of_tries])
    print(show_hidden_word(secret_word, old_letter_guessed))

    while num_of_tries < MAX_TRIES:

        guessed_letter = input("guess a letter: ")
        # check if input is valid
        while not try_update_letter_guessed(guessed_letter, old_letter_guessed):
            guessed_letter = input("invalid input, please try again. guess a letter: ")

        # check if the letter guessed is in the secret word
        if guessed_letter not in secret_word:
            num_of_tries += 1
            print(f":(\n{HANGMAN_PHOTO[num_of_tries]}")

        print(show_hidden_word(secret_word, old_letter_guessed))

        # check win
        if check_win(secret_word, old_letter_guessed):
            print('WIN')
            break

    # check lose
    print(num_of_tries)
    if num_of_tries == MAX_TRIES:
        print('LOSE')

if __name__ == '__main__':
    main()
