
#Irvin Silva	
class Player_Input():
    '''
	This class is responsible for keeping track of the player's input, determining if the player's 
	input is in the random word.
	'''
    def __init__(self,hidden_word=["c","a","t"]):
        self.hidden_letters=hidden_word
        self.player_input=input("Guess a letter [a-z]: ")
    
    def input_in_hidden_word(self):
        '''
        This method verifies if the player's input is found in a of list letters of the hidden word
        '''
        for i in self.hidden_letters:
            if i in self.player_input:
                #print(i)
                return i
            else:
                #print("garbage")
                return False

#test=Player_Input()
#test.input_in_hidden_word()