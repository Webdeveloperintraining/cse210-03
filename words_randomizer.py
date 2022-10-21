import random

class WordRandomizer():

    def __init__(self):
        '''
            set our variables used throughout the class
        '''
        self._word_list = [
                'moroni',
                'mormon',
                'alma',
                'nephi',
                'helaman',
                'omnipotent',
                'mosiah',
                'lamanites',
                'lord',
                'moses',
                'judgments',
                'angel',
                'lord',
                'commandments',
                'guitar',
                'zoramites']
    

    def get_word(self):
        word = random.choice(self._word_list).lower()

        letters=[]
        for i in word:
            letters.append(i)

        return letters
        





# word_list = [
#     'moroni',
#     'mormon',
#     'alma',
#     'nephi',
#     'helaman',
#     'omnipotent',
#     'mosiah',
#     'lamanites',
#     'lord',
#     'moses',
#     'judgments',
#     'angel',
#     'lord',
#     'commandments',
#     'guitar',
#     'zoramites']

# def get_word():
#     word = random.choice(word_list)
#     return word.upper()

