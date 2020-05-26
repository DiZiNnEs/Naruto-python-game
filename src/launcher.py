from tkinter import *

from src.game_modes.singe_player import start_game as single_game
from src.game_modes.game_for_two_players import start_game as two_game
from src.game_modes.game_for_three_players import start_game as three_game
from src.game_modes.game_for_four_players import start_game as four_game
from src.game_modes.game_for_five_players import start_game as five_game
from src.game_modes.game_for_six_players import start_game as six_game

root = Tk(className='Launcher')


def end_game():
    return root.destroy()


def start_the_game():
    root.geometry('300x300')
    myLabel = Label(root, text='Naruto Game!').pack()
    single_player = Button(root, text='Single player', command=single_game, fg='black').pack()
    game_for_two = Button(root, text='Game for two players', command=two_game, fg='black').pack()
    game_for_three = Button(root, text='Game for three players', command=three_game, fg='black').pack()
    game_for_four = Button(root, text='Game for four players', command=four_game, fg='black').pack()
    game_for_five = Button(root, text='Game for five players', command=five_game, fg='black').pack()
    game_for_six = Button(root, text='Game for six players', command=six_game, fg='black').pack()
    exit_button = Button(root, text='EXIT', command=end_game, fg='black').pack()

    root.mainloop()


if __name__ == '__main__':
    start_the_game()
