
class Hangman:
    MAX_TRIES = 6
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

    def __init__(self, secret_word : str, max_tries=6):
        self.max_tries = max_tries
        self.letters_guessed = []
        self.num_of_tries = 0
        self.secret_word = secret_word
    
    def is_game_over(self):
        return self.check_win() or self.num_of_tries >= self.max_tries
    
    def check_win(self) -> bool:
        for letter in self.secret_word:
            if not letter in self.letters_guessed:
                return False
            
        return True
    
    def show_hidden_word(self) -> str:
        output = []
        for letter in self.secret_word:
            if letter in self.letters_guessed:
                output.append(letter)
            else:
                output.append('_')
                
        return ' '.join(output)
    
    def check_valid_input(self, guess: str) -> bool:
        is_letter = Hangman.is_letter(guess)
        if not is_letter or guess in self.letters_guessed:
            print(f"X\n{'->'.join(self.letters_guessed)}")
            return False

        return True
    
    def check_correct_guess(self, guess: str) -> bool:
        return guess in self.secret_word
    
    def handle_incorrect_guess(self):
        self.num_of_tries += 1
        print(f":(\n{Hangman.HANGMAN_PHOTOS[self.num_of_tries]}\n")
        
    def handle_valid_guess(self, guess: str):
        self.letters_guessed.append(guess.lower())
           
    @staticmethod
    def is_letter(letter: str) -> bool:
        if len(letter) == 1:
            return letter.isalpha()
        return False
    
    