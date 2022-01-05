from turtle import Screen, Turtle
import pandas


def state_game_start():
    screen = Screen()
    turtle = Turtle()
    img = "state_game/blank_states_img.gif"
    screen.addshape(img)
    turtle.shape(img)
    turtle_move = Turtle()
    turtle_move.penup()
    turtle_move.hideturtle()
    states_cords = pandas.read_csv("state_game/50_states.csv")
    all_states = states_cords.state.to_list()

    guessed = []
    while len(guessed) < 50:
        name = screen.textinput(title=f"Guess the States {len(guessed)}/50", prompt="What's another state's name?")
        cords = states_cords[states_cords.state == name.title()]
        if name.title() == "Exit":
            break
        if not cords.empty:
            turtle_move.goto(int(cords.x), int(cords.y))
            guessed.append(name.title())
            turtle_move.write(name.title())
    if len(guessed) == 50:
        turtle_move.goto(-100, 0)
        turtle_move.write("Congratulations, you guessed all 50 states!!!")
    else:
        unguessed = [state for state in all_states if not (state in guessed)]
        missing = {"States": unguessed}
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("state_game/missing_states")

    screen.exitonclick()
