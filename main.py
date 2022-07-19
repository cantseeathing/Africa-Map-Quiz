import turtle
import score_board
import main_screen
import data_control
import country_draw

DATABASE = "finished_list.csv"
BACKGROUND = "africa-map_gif.gif"
SCREEN_SIZE = (700, 723)
ANSWER_LIST = []

screen = main_screen.MainScreen(screen_size=SCREEN_SIZE, background=BACKGROUND).ask()
data_base, INDEX = data_control.Data(source=DATABASE).data_base()
score = score_board.Score(screen_size=SCREEN_SIZE, length=INDEX)
draw_object = country_draw.Draw()
found_countries = []
print(f"There is a total of {INDEX} countries")
while len(found_countries) < INDEX:
    answer = str(screen.textinput(title="Guess a Country",
                                  prompt="Please enter the name of a country in Africa:")).capitalize()
    print(answer)
    if answer in list(data_base['Country']):
        if answer in ANSWER_LIST:
            print("answer exist already")
        else:
            print(data_base[data_base['Country'] == answer])
            x = int(data_base[data_base['Country'] == answer]['X'])
            y = int(data_base[data_base['Country'] == answer]['Y'])
            ANSWER_LIST.append(answer)
            found_countries = draw_object.draw_country(x=x, y=y, name=answer)
            print(f"you have {INDEX - len(found_countries)} countries left to guess!")
            score.update_score()
    elif answer == "Exit" or answer == "":
        print("Quitting the game..")
        screen.exitonclick()
        break
    else:
        print("Incorrect answer")
if INDEX == len(found_countries):
    print("Congrats! you win!!")
# print(data_base[data_base['Country'] == ANSWER_LIST[0]]['X'][0])
turtle.mainloop()

# turtle.mainloop()
