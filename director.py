'''
file: director.py

this file houses the director class that is in charge of the game operations
'''

from player_input import Player_Input
from words_randomizer import WordRandomizer
from draw_jumper import DrawJumper
from letters_output import Letters_output

class Director():
    '''
        This class has the responsibility to run all other classes as well as make the game work properly
        as stated in the program requirements. 
	'''

    def __init__(self):
        self._playing_game = True
        self._wrong_guesses = 0
        self._correct_guess = False
        self._player_input = ''

        self._random_word_gen = WordRandomizer()
        self._random_word = self._random_word_gen.get_word()
        self._terminal_service = Player_Input(self._random_word)
        self._draw_jumper = DrawJumper()
        self._word_output = Letters_output(self._random_word)


    def start_game(self):
        '''
            This function is in charge of starting the game and running the game
        '''
        print('starting game')
        self._show_output()
        # self._word_output.clear_underscore(self._player_input)

        
        while self._playing_game:
            self._get_inputs()
            self._update_game()
            self._show_output()

        print('Game Over...')
        self._play_again()
        
        

    
    def _get_inputs(self):
        '''
            this function gets input from the user and validates it
        '''
        user_input = self._terminal_service.input_in_hidden_word()
        if user_input:
            self._correct_guess = True
            self._player_input = user_input

        else:
            self._correct_guess = user_input


    def _update_game(self):
        '''
            updates the game board
        '''


        if not self._correct_guess:
            self._wrong_guesses = self._wrong_guesses + 1

        if self._wrong_guesses >= 4:
            self._playing_game = False
            print('\n\nYou lost...')
            

    def _show_output(self):
        '''
            once game has been updated the output can then be shown to the user
        '''
        print(self._wrong_guesses)

        self._draw_jumper.print_jumper(self._wrong_guesses)

        player_not_won = self._word_output.print_places(self._player_input)

        if not player_not_won:
            self._playing_game = False
            print('\n\nYou WON!')


    def _play_again(self):
        play_again = ''
        while True:
            play_again = input('Would you like to play again? (y, n): ').strip().lower()
            if play_again == 'y':

                self._playing_game = True
                self._wrong_guesses = 0
                self._correct_guess = False
                self._player_input = ''

                self._random_word = self._random_word_gen.get_word()

                self._terminal_service.hidden_letters = self._random_word
                self._terminal_service.clear_words_used_list()
                # self._word_output.clear_underscore()
                self._word_output.clear_underscore(self._random_word)
                self.start_game()
            else:
                print('Good bye!')
                break