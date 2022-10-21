

class DrawJumper():

    def __init__(self):

        self._drawings = ['''
    _____
   /_____\\
   \     /
    \   /
      0
     /|\\
     / \\
        
^^^^^^^^^^^^^^^
        ''',
        '''
    
   /_____\\
   \     /
    \   /
      0
     /|\\
     / \\
        
^^^^^^^^^^^^^^^
        ''',
        '''
    

   \     /
    \   /
      0
     /|\\
     / \\
        
^^^^^^^^^^^^^^^
        ''',
        '''
   


    \   /
      0
     /|\\
     / \\
        
^^^^^^^^^^^^^^^
        ''',
        '''
    



      x
     /|\\
     / \\
        
^^^^^^^^^^^^^^^
        ''']

    def print_jumper(self, wrong_guesses):
        print(self._drawings[wrong_guesses])