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

        # this is the main loop for the game to keep running
        while self._playing_game:
            self._get_inputs()
            self._update_game()
            self._show_output()

        # when the loop is broke it will end the game 
        # this can happen from losing or winning
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
            updates the game board, checks if user guess wrong or lost the gamed
        '''

            # checks if the user guessed correctly or not
        if not self._correct_guess:
                # if user guessed wrong a point is added 
            self._wrong_guesses = self._wrong_guesses + 1

            # if the user gets 4 or more wrong guesses the game is over
        if self._wrong_guesses >= 4:
            self._playing_game = False
            print('\n\nYou lost...')
            

    def _show_output(self):
        '''
            once game has been updated the output can then be shown to the user
            this is for drawing the stickman jumper and the word 
        '''

            # draws the jumper to the screen
        self._draw_jumper.print_jumper(self._wrong_guesses)

            # checks if the player has won the game
            # also draws the word to the screen
        player_not_won = self._word_output.print_places(self._player_input)

            # if the player has won the game is over
        if not player_not_won:
            self._playing_game = False
            print('\n\nYou WON!')


    def _play_again(self):
        '''
            This function is run after the game is over and the player has won or lost
            it will check with the player if they want to play again or leave the game
        '''

        play_again = ''
        while True:
            play_again = input('Would you like to play again? (y, n): ').strip().lower()

                # checks if the user wants to play again
                # if they do the game is reset
            if play_again == 'y':

                break

                # if the user does not want to play then game is over
                # and the program ends
            elif play_again == 'n':
                print('Good bye!')
                return False
            else:
                print('Enter a valid choice please.')

        self._restart_game()

    def _restart_game(self):
        self._playing_game = True
        self._wrong_guesses = 0
        self._correct_guess = False
        self._player_input = ''

            # gets a new random word for the new game
        self._random_word = self._random_word_gen.get_word()

            # updates the random word for the player to guess
        self._terminal_service.hidden_letters = self._random_word
            # clears the list of used letters so player can guess again
        self._terminal_service.clear_words_used_list()

            # clears the word so that it can display the new word
        self._word_output.clear_underscore(self._random_word)

            # calls the start game function for the game to start again
        self.start_game()