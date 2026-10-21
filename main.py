from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

# ___________________________________________Words Interactivity___________________________________________
to_learn = {}
current_card = {}


try:
    dataframe = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = dataframe.to_dict(orient="records")

# Deleting correct words from our list
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# Change the text
def next_card():
    global current_card, timer

    window.after_cancel(timer)

    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Finished!")
        canvas.itemconfig(card_word, text="You've learned all of the words!")
        canvas.itemconfig(canvas_img, image=card_front_img)
        return

    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)

    timer = window.after(3000, new_image)


# change the image
def new_image():
    global current_card, timer

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)

    timer = window.after(3000, old_image)

def old_image():
    global current_card, timer

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)

    timer = window.after(3000, new_image)

# _________________________________UI_________________________________
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, new_image)

# Canvas
# Image
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)

canvas_img = canvas.create_image(400, 263, image=card_front_img)


# Text
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")

canvas.grid(row=0, column=0, columnspan=2)


# Buttons
right_img = PhotoImage(file="images/right.png")
known_button = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)

known_button.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)

unknown_button.grid(row=1, column=1)

next_card()



window.mainloop()
