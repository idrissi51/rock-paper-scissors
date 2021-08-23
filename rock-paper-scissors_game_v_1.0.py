# import modules
from tkinter import *
import random

# window
root = Tk()
root.geometry("400x400")
root.title("Rock-Paper-Scissors")
Label(root, text="Rock,Paper,Scissors",
      font="arial 20 bold", bg="seashell2").pack()
Label(root, text="Choose any one: rock,paper,scissors",
      font="arial 15", bg="seashell2").place(x=30, y=60)

# user_choose
user_take = StringVar()
Entry(root, textvariable=user_take,
      bg="antiquewhite2", width=50).place(x=45, y=100)

Result = StringVar()
# computer_choose
words = ["rock", "paper", "scissors"]
computer_choose = random.choice(words)

# Play


def play():
    user_pick = user_take.get()
    if user_pick == computer_choose:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and computer_choose == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and computer_choose == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and computer_choose == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and computer_choose == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and computer_choose == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and computer_choose == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set("invalid: choose any one -- rock, paper, scissors")
# rest function


def rest():
    Result.set("")
    user_take.set("")


def quit():
    root.destroy()


Button(root, text="PLAY", command=play, font="arial 13 bold",
       bg="seashell4").place(x=170, y=140)
Entry(root, textvariable=Result, bg="antiquewhite2", width=50).place(x=45, y=220)
Button(root, text="RESET", font="arial 13 bold",
       bg="seashell4", command=rest).place(x=30, y=300)
Button(root, text="EXIT", font="arial 13 bold",
       bg="seashell4", command=quit).place(x=300, y=300)

root.mainloop()
