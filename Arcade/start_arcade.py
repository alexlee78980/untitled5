from snake_game.snake_main import snake_start
from state_game.state_guess_game import state_game_start
from pong.pong_start import pong_start
from turtle_crossing.turtle_crossing_start import turtle_crossing_start
from turtle_race.turtle_race_start import turtle_race_start
import tkinter


def start_arcade():
    window = tkinter.Tk()
    window.title("Arcade")
    label = tkinter.Label(text="Arcade", font=("Courier", 50, "bold"))
    label.grid(column=1, row=0)

    # pong
    def pong():
        window.destroy()
        pong_start()

    photo_pong = tkinter.PhotoImage(file="images/pong.gif")
    photo_pong = photo_pong.subsample(3, 3)

    label_pong = tkinter.Label(text="Pong", font=("Courier", 20, "bold"))
    label_pong.grid(column=0, row=1)
    button_pong = tkinter.Button(image=photo_pong, command=pong)
    button_pong.grid(column=0, row=2)

    # snake_game
    def snake_game():
        window.destroy()
        snake_start()

    photo_snake = tkinter.PhotoImage(file="images/snake_image.PNG")
    photo_snake = photo_snake.subsample(9, 9)

    label_snake = tkinter.Label(text="Snake Game", font=("Courier", 20, "bold"))
    label_snake.grid(column=1, row=1)
    button_snake = tkinter.Button(image=photo_snake, command=snake_game)
    button_snake.grid(column=1, row=2)

    # state_game
    def state_game():
        window.destroy()
        state_game_start()

    photo_state = tkinter.PhotoImage(file="images/state_image.PNG")
    photo_state = photo_state.subsample(9, 9)

    label_state = tkinter.Label(text="Guess State", font=("Courier", 20, "bold"))
    label_state.grid(column=2, row=1)
    button_state = tkinter.Button(image=photo_state, command=state_game)
    button_state.grid(column=2, row=2)

    # turtle_race
    def race():
        window.destroy()
        turtle_race_start()

    photo_race = tkinter.PhotoImage(file="images/race_image.PNG")
    photo_race = photo_race.subsample(6, 6)

    label_race = tkinter.Label(text="Turtle Race", font=("Courier", 20, "bold"))
    label_race.grid(column=0, row=3)
    button_race = tkinter.Button(image=photo_race, command=race)
    button_race.grid(column=0, row=4)

    # turtle_crossing

    def crossing():
        window.destroy()
        turtle_crossing_start()

    photo_crossing = tkinter.PhotoImage(file="images/crossing_image.PNG")
    photo_crossing = photo_crossing.subsample(9, 9)

    label_crossing = tkinter.Label(text="Turtle Crossing", font=("Courier", 20, "bold"))
    label_crossing.grid(column=1, row=3)
    button_crossing = tkinter.Button(image=photo_crossing, command=crossing)
    button_crossing.grid(column=1, row=4)
    window.mainloop()
