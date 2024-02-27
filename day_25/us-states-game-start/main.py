# New york states finding game

import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

# Get X, Y coordinates when mouse click from screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


def write_to_map(state_name, xcor, ycor):
    # print(state_name)
    # print(xcor)
    # print(ycor)
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.goto(xcor, ycor)
    writer.write(answer_state)


def create_csv_with_missed_states(all_states, guessed_states):
    missed_states = []
    for state in all_states:
        if state not in guessed_states:
            missed_states.append(state)
    missed_dict = {
        "State": missed_states
    }
    df = pandas.DataFrame(missed_dict)
    df.to_csv("excluded_states.csv")


correct_states = []
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    # print(answer_state)
    if answer_state == "Exit":
        create_csv_with_missed_states(states_list, correct_states)
        break
    if answer_state == "" and answer_state is None:
        continue
    if answer_state in states_list and answer_state not in correct_states:
        correct_states.append(answer_state)
        answer_state_data = states_data[states_data.state == answer_state]
        # print("answer_state_data: \n", answer_state_data)
        answer_state_xcor = answer_state_data.x.item()
        answer_state_ycor = answer_state_data.y.item()
        # print("answer_state_x: \n", answer_state_xcor)
        # print("answer_state_y: \n", answer_state_ycor)
        write_to_map(answer_state, answer_state_xcor, answer_state_ycor)

