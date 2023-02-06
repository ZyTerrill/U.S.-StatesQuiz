import turtle
import pandas

# Using US map as turtle shape
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Assigning 50_states.csv data to data variable
data = pandas.read_csv('50_states.csv')

# Converting csv States to a list
all_states = data.state.to_list()
guessed_states = []

# Main loop
while len(guessed_states) < 50:
    # Asking for user input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correctt",
                                    prompt="What's another state's name?").title()

    # Creating csv file for studying
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('States to learn')
        break
    # Checking user input and writing State name
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

