import sys, os, random
import pygame
import SCORES, CONST


hiscores = None

def game_entry():
    game_init()
    game_mainloop()

def game_init():
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    global hiscores
    hiscores = SCORES.SCORES(main_dir)
    hiscores.load()
    hiscores.new_game()

    hiscores.add_lines(3)
    hiscores.add_lines(2)
    hiscores.end_game("Player")



def game_mainloop():
    while True:
        pass



if __name__ == '__main__':
    game_entry()
