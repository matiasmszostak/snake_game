from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
FILE_PATH = "highest_score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(FILE_PATH, mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} - Highest Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        with open(FILE_PATH, mode="w") as file:
            if self.score > self.highscore:
                self.highscore = self.score
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
