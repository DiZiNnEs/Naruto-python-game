from game import start_game as game

from tkinter import *

root = Tk(className='Launcher')


def end_game():
    return root.destroy()


def start_game2():
    root.geometry('300x100')
    myLabel = Label(root, text='Naruto Game!').pack()
    myButton = Button(root, text='Start game', command=game, fg='black').pack()
    exit_button = Button(root, text='EXIT', command=end_game, fg='black').pack()

    root.mainloop()


if __name__ == '__main__':
    start_game2()
