import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

guessed_states = []
states_to_learn = states

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="type the name of a state").title()
    if answer_state == "Exit":
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("States_to_Learn")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        states_to_learn.remove(answer_state)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        xcor = data[data["state"] == answer_state]["x"].to_list()
        ycor = data[data["state"] == answer_state]["y"].to_list()
        turtle.goto(xcor[0], ycor[0])
        turtle.write(arg=answer_state, align="center", font=("arial", 10, "normal"))


