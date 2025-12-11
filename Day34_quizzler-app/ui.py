from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.score = 0
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.geometry("350x600")  # Width x Height

        # Option 1: Using a color name
        self.window.configure(bg=THEME_COLOR)

        # labels
        self.score_label = Label(text=f'Score: {self.score}', highlightthickness=0, background=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, background='white', highlightthickness=0)
        self.question_text= self.canvas.create_text(150, 125,width=280, text="French", font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        right_image = PhotoImage(file='./images/true.png')
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.check_answer_true)
        self.right_button.grid(row=2, column=0, pady=20, padx=20)

        wrong_image = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.check_answer_false)
        self.wrong_button.grid(row=2, column=1,pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            qText = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = qText)
        else:
            self.canvas.itemconfig(self.question_text, text='You''ve reached the end of the quiz!')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def check_answer_true(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def change_to_white(self):
        self.canvas.config(background='white')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.window.after(1000,self.get_next_question)





