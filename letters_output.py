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

        is_there = isinstance(match_letter, str)
        
        if is_there:
            if match_letter == False or match_letter == "":
                pass
            else:
                index = self.letters_list.index(match_letter)
                self.underscores[index] = match_letter

    def print_places (self, match_letter):
        self.appends_underscores()
        self.replace_underscores(match_letter)
        print(*self.underscores)




