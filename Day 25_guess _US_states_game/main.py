import turtle
import pandas

def get_mouse_click_coordinates(x, y):
    print(x,y)
IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S States Game: Name the States")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")


is_game_on = True
guessed_states = []
states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

    if answer == 'Exit':
        break

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        answer_row = states_data[states_data.state == answer]
        writer.goto(answer_row.x.item(), answer_row.y.item())
        writer.write(answer, align="center", font=("Arial", 10, "normal"))

not_guessed_states = list(set(states).difference(guessed_states))
not_guessed_states_df = pandas.DataFrame(not_guessed_states)
not_guessed_states_df.columns = ['Missed States']
not_guessed_states_df.to_csv('states_to_learn.csv')