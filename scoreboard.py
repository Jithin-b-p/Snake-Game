from turtle import Turtle

# constants for score displaying.
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.retrieve_high_score()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.show_score()

    def retrieve_high_score(self) -> int:
        with open("high_score.txt") as file:
            high_score = int(file.read())
        return high_score

    def update_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_high_score()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()
