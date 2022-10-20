'''
file: director.py

this file houses the director class that is in charge of the game operations
'''


from player_input import Player_Input

class Director():
    '''
        This class has the responsibility to run all other classes as well as make the game work properly
        as stated in the program requirements. 
	'''

    def __init__(self):
        self._playing_game = True
        self._terminal_service = Player_Input()

    def start_game(self):
        '''
            This function is in charge of starting the game and running the game
        '''
        while self._playing_game:
            self._get_inputs()
            self._update_game()
            self._show_output()

    
    def _get_inputs(self):
        '''
            this function gets input from the user and validates it
        '''
        user_input = self._terminal_service.input_in_hidden_word()
        print(user_input)

    def _update_game(self):
        '''
            updates the game board
        '''

    def _show_output(self):
        '''
            once game has been updated the output can then be shown to the user
        '''