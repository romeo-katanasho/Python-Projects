from tkinter import *
import pandas
import random
import time
BACK_GROUND_COLOR = "#B1DDC6"

DataFrame = pandas.read_csv("words2learn.csv")
to_learn = DataFrame.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text= current_card["French"], fill="black")
    canvas.itemconfig(card_background, image = card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text ="English",fill = "white")
    canvas.itemconfig(card_word, text =current_card["English"],fill = "white")
    canvas.itemconfig(card_background, image = card_back_image)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("words2learn.csv")
#===============================UI SECTION==================================
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACK_GROUND_COLOR)
flip_timer = window.after(3000, flip_card)

right = PhotoImage(file="right.png")
wrong = PhotoImage(file="wrong.png")
card_front_image = PhotoImage(file="card_front.png")
card_back_image = PhotoImage(file="card_back.png")

canvas = Canvas(width=800, height=526 , highlightthickness=0)
card_background = canvas.create_image(400, 263,image=card_front_image)
canvas.config(bg=BACK_GROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 48, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

button_right = Button(image=right, bg=BACK_GROUND_COLOR, highlightthickness=0, command= is_known)
button_right.grid(column=0, row=1)
button_wrong = Button(image=wrong, bg=BACK_GROUND_COLOR, highlightthickness=0, command= next_card)
button_wrong.grid(column=1, row=1)

next_card()

#===============================UI SECTION==================================

window.mainloop()