from question_model import Question
#from data import question_data
from TriviaDb import question_data
from quiz_brain import QuizBrain

question_bank = []
for d in question_data:
    #question = Question(d['text'], d['answer'])
    question = Question(d['question'], d['correct_answer'])
    question_bank.append(question)


quiz_brain1 = QuizBrain(question_bank)

while quiz_brain1.still_has_questions():
    quiz_brain1.next_question()

print(f"You've completed the quiz \nYour final score is {quiz_brain1.score}/{quiz_brain1.question_number}")

