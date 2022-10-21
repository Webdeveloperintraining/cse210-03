#Irvin Silva	
class Player_Input():
    '''
	This class is responsible for keeping track of the player's input, determining if the player's 
	input is in the random word.
	'''
    def __init__(self,hidden_word=["c","a","t"]):
        self.hidden_letters=hidden_word
        self._player_input=input("Guess a letter [a-z]: ").lower()
        self._words_used=[]
    
    def input_in_hidden_word(self):
        '''
        This method verifies if the player's input is a letter from the the hidden word.
        '''
        self.verify_not_repeated_word()

        for i in self.hidden_letters:

            if i in self._player_input:
                return i

        return False

    def verify_not_repeated_word(self):
        '''
        This method verifies there isn't a letter that has already already typed by the player.
        '''
        while self._player_input in self._words_used:
            self._player_input=input("Guess a letter [a-z]: ").lower()
        if self._player_input not in self._words_used:
            self._words_used.append(self._player_input)

    def clear_words_used_list(self):
        self._words_used.clear()
        #print(self._words_used)

# test=Player_Input()
# test.input_in_hidden_word()
# test.input_in_hidden_word()
# print(test._words_used)
# test.clear_words_used_list()
