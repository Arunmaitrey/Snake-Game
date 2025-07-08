from turtle import Turtle
AlIGNMENT="center"
FONT=("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("abc.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

        # def game_over(self):
        #     self.goto(0,0)
        #     self.write("GAME OVER",align=AlIGNMENT,font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} High Score:{self.high_score}", align=AlIGNMENT, font=FONT)


    def count_score(self):
        self.clear()
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("abc.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()



