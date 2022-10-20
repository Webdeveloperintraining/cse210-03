import random
word_list = [
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

def get_word():
    word = random.choice(word_list)
    return word.upper()

