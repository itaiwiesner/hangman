from NotAbcLetterError import NotAbcLetterError
from hangman_logic import Hangman

FILE_PATH = 'words.txt'


def choose_word(index: int) -> str:
    with open(FILE_PATH) as f:
        words = f.read().split()
        
        while index >= len(words):
            index -= len(words)
            
        return words[index]
    
def print_home_screen():
    print("""Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")
    print(Hangman.MAX_TRIES)

def main():
    print_home_screen()
    index = input("choose index: ")
    while not index.isnumeric():
        index = input("choose index: ")

    secret_word = choose_word(int(index))
    
    hangman_logic = Hangman(secret_word, Hangman.MAX_TRIES)
    print("let's get started!")
    while not hangman_logic.is_game_over():
        guess = input("enter your guess: ") 
        is_valid = hangman_logic.check_valid_input(guess)
        while not is_valid:
            guess = input("enter your guess: ")
            is_valid = hangman_logic.check_valid_input(guess)
            
        hangman_logic.handle_valid_guess(guess)
        is_correct = hangman_logic.check_correct_guess(guess)
        if not is_correct:
            hangman_logic.handle_incorrect_guess()
            
        print(hangman_logic.show_hidden_word())
        
    if hangman_logic.check_win():
        print("WIN")
    else:
        print("LOSE")
        
if __name__ == '__main__':
    main()
