import os
import CONST

import pickle


class SCORES:
    def __init__(self,main_dir):
        self.main_dir = main_dir
        self.data = {}

    def new_game(self):
        self.score = 0
        self.level = 1
        self.lines_left_to_the_next_level = CONST.LEVEL_PER_LINE

    def end_game(self):
        pass

    def save(self,filename):
        with open(filename, 'wb') as f:
             pickle.dump(self.data, f)

    def load(self):
        hiscores = os.path.join(self.main_dir,CONST.HISCORES_FILENAME)
        if not os.path.exists(hiscores):
            self._defaults()
            self.save(hiscores)
        else:
            with open(hiscores, 'rb') as f:
                self.data = pickle.load(f)
                breakpoint()

    def _defaults(self):
        self.data = dict(zip(['Bob','Helen','John','Ed','Yuriy','Jane','Oliver','Alex','Wayne','Dmitriy'],[10000,9000,8000,7000,6000,5000,4000,3000,2000,1000]))

    def add_lines(self, lines):
        self.score += CONST.SCORE_PER_LINE[lines-1]
