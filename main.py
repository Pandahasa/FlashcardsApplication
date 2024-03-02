BACKGROUND_COLOR = "#B1DDC6"

import random
import time
from tkinter import *
import pandas

# -flip function-
def next():
    global gen 
    gen = random.randint(0 , len(English))
    canvas.itemconfig(card , image = card_front)
    canvas.itemconfig(language , text="French" , fill="black")
    canvas.itemconfig(word , text=French[gen] , fill="black")
    window.after(3000 , func=flip)



def flip():
    canvas.itemconfig(language , text="English" , fill="white")
    canvas.itemconfig(word , text=English[gen] , fill="white")
    canvas.itemconfig(card , image = card_back)


# -correct/incorrect function   

def right():
    data.drop(index=gen , inplace=True)
    del French[gen]
    del English[gen]
    print(data)
    data.to_csv("french_words.csv" , index = False)
    next()

# -other code
name = "french_words.csv"
data = pandas.read_csv(name)

French = {index:row.French for (index , row) in data.iterrows()}
English = {index:row.English for (index , row) in data.iterrows()}

# ui_setup

window = Tk()
window.title("Flashy")
window.config(padx= 50 , pady = 50 , background = BACKGROUND_COLOR)


canvas = Canvas(width= 800 , height = 526 , background= BACKGROUND_COLOR , highlightthickness=0)


card_front = PhotoImage(file = "card_front.png")
card_back = PhotoImage(file = "card_back.png")
card = canvas.create_image(400, 263 , image = card_front)
language = canvas.create_text(400 , 150 , text="" , fill="white", font=("Arial" , 40 , "italic"))
word = canvas.create_text(400 , 263 , text="" , fill="white", font=("Arial" , 60 , "bold"))
canvas.grid(column = 0 , row = 0 , columnspan= 2)
next()


wrong_png = PhotoImage(file = "wrong.png")
wrong_button = Button(image = wrong_png , command = next)
wrong_button.grid(column = 0 , row = 1)

right_png = PhotoImage(file = "right.png")
right_button = Button(image = right_png , command = right)
right_button.grid(column = 1 , row = 1)



window.mainloop()