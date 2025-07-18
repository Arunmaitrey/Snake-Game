
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")

screen.title("SnakeGame")
screen.tracer(0)
turtles=[]

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)


#detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.count_score()
        snake.extend_turtle()


    #detect collisions with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.xcor()<-280:
        scoreboard.reset()
        snake.reset_snake()


    #detect collision with tail
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle)<10:
            scoreboard.reset()
            snake.reset_snake()
        

    snake.move()








screen.exitonclick()