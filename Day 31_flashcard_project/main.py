from tkinter import *
import pandas
import random

BACKGROUND_COLOR = '#B7E5CD'
FILL_COLOR_BLACK = "black"
FILL_COLOR_WHITE = "white"
data_frame = None
data_list =[]
current_card = {}
try:
    data_frame = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data_frame = pandas.read_csv('./data/french_words.csv')
    data_list = data_frame.to_dict(orient="records")
else:
    data_list = data_frame.to_dict(orient="records")

# -- get random word to guess --
def get_random_word():
    global current_card, flip_timer, data_frame
    window.after_cancel(flip_timer)

    current_card = random.choice(data_list)

    canvas.itemconfig(language_text, text="French", fill=FILL_COLOR_BLACK)
    canvas.itemconfig(word_text, text=current_card['French'], fill = FILL_COLOR_BLACK)
    canvas.itemconfig(card_background, image=front_card_image)

    flip_timer=window.after(3000, func=flip_card)

# -- flip --
def flip_card():
     canvas.itemconfig(language_text, text="English", fill=FILL_COLOR_WHITE)
     canvas.itemconfig(word_text, text=current_card['English'], fill=FILL_COLOR_WHITE)
     canvas.itemconfig(card_background, image=back_card_image)

def is_known():
    data_list.remove(current_card)
    df = pandas.DataFrame(data_list)
    df.to_csv('data/words_to_learn.csv', index=False)
    get_random_word()

window = Tk()
window.title("flashy")
window.config(padx=50, pady=20, background = BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card_image = PhotoImage(file='./images/card_front.png')
back_card_image = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image=front_card_image)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel",30,"italic"), fill= FILL_COLOR_BLACK)
word_text = canvas.create_text(400, 263, text="French", font=("Ariel",50,"bold"), fill= FILL_COLOR_BLACK)
canvas.config(highlightthickness = 0, background = BACKGROUND_COLOR)
canvas.grid( row=0, column=0, columnspan=2)
get_random_word()

wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_random_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file='./images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)


window.mainloop()