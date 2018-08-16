import os
import pickle
import CONST


class SCORES:
    def __init__(self,main_dir):
        self.filename = os.path.join(main_dir,CONST.HISCORES_FILENAME)
        self.data = {}
        self.sorted = []

    def new_game(self):
        self.score = 0
        self.level = 1
        self.lines_to_next_level = CONST.LINES_PER_LEVEL

    def end_game(self, playername):
        self.data[playername]=self.score
        self.save()

    def save(self):
        self._make_sorted()
        self.data.clear()
        for name,score in self.sorted:
            self.data[name]=score
        with open(self.filename, 'wb') as f:
             pickle.dump(self.data, f)

    def load(self):
        if not os.path.exists(self.filename):
            self._defaults()
            self.save()
        else:
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)
        self._make_sorted()

    def _defaults(self):
        self.data = dict(zip(['Bob','Helen','John','Ed','Yuriy','Jane','Oliver','Alex','Wayne','Dmitriy'],[10000,9000,8000,7000,6000,5000,4000,3000,2000,1000]))

    def add_lines(self, lines):
        self.score += CONST.SCORE_PER_LINE[lines-1]

    def _make_sorted(self):
        self.sorted = sorted(self.data.items(), key=lambda kv: kv[1], reverse = True)[:CONST.HISCORES_LIMIT]
