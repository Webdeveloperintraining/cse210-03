class Letters_output():

    def __init__(self, letters_list = ["c","a","t"]):

        self.letters_list = letters_list
        self.word_length = len(letters_list)
        self.underscores = []
        self.lits_length = len(self.underscores)


    
    def appends_underscores(self):

        if self.lits_length == 0:
            for i in range(self.word_length):
                self.underscores.append("_")

    
    def replace_underscores (self, match_letter):

        # is_there = isinstance(match_letter, str)
        # if is_there:
        index = 0
        for letter in self.letters_list:
            if match_letter == letter:
                self.underscores[index] = match_letter
            index += 1

            # if match_letter == False or match_letter == "":
            #     pass
            # else:
            #     index = self.letters_list.index(match_letter)
            #     self.underscores[index] = match_letter

    def print_places (self, match_letter):
        if len(self.underscores) == 0:
            self.appends_underscores()
        self.replace_underscores(match_letter)
        print(*self.underscores)
        
        return self.check_win()

    def clear_underscore(self, new_word):
        self.underscores.clear()
        self.letters_list = new_word
        self.word_length = len(self.letters_list)
        self.lits_length = len(self.underscores)
    
    def check_win(self):
        still_underscore = True
        for letter in self.underscores:
            if letter == '_':
                still_underscore = True
                return still_underscore

        return False



