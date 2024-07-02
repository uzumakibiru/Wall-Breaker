import turtle
from random import choice

ball_speed=2
game_on =True
#List for changing direction after collison with the ceiling
set_heading=[315,225]
score_list=[]
ceiling_list=[]


screen=turtle.Screen()
screen.title("Wall Breaker")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

#Create a Ball
ball=turtle.Turtle(shape="circle")
ball.color("white")
ball.penup()
ball.setheading(270)
    
#Create the walls:

def create_wall():
        x=-320
        y=250
        
        while x<350:
            
            for i in range(6):
                y-=30
                wall(x,y)
                if i ==5:
                    y=250
            x+=90  
        if  x>350:
            return
        wall(x,y)
    
#Walls     
def wall(x,y):
        ceiling=turtle.Turtle(shape="square")
        ceiling.color("white")
        ceiling.shapesize(stretch_len=4)
        ceiling.penup()
        ceiling.goto(x,y)
        ceiling_list.append(ceiling)
        score_list.append(ceiling)
        
#Create a paddle
paddle=turtle.Turtle(shape="square")
paddle.color("white")
paddle.shapesize(stretch_wid=1,stretch_len=5)
paddle.penup()
paddle.hideturtle()
paddle.goto(0,-250)
paddle.showturtle()

#Move the paddle right
def movement_right():
    pos_paddle=paddle.xcor()
    pos_paddle+=50
    if pos_paddle > 350:
        pos_paddle=350
        
    paddle.setx(pos_paddle)
#Move the paddle left
def movement_left():
    pos_paddle=paddle.xcor()
    pos_paddle-=50
    if pos_paddle <-350:
        pos_paddle=-350
    
    paddle.setx(pos_paddle)
#Listen for the keyboard entry left or right
def control_paddle():
    screen.listen()
    screen.onkey(movement_right,"Right")
    screen.onkey(movement_left,"Left")


#Collison detection  
def collison():
    #Detcting paddle collison and generating random heading direction
    paddle_coll=[45,135]
    x_pad,y_pad=paddle.pos()
    x_ball,y_ball=ball.pos()
    if abs(y_ball-y_pad)<20 and  abs(x_ball-x_pad)<50:
        ball.setheading(choice(paddle_coll))
        
            
        
    
    #Iterating the walls to check if the ball has collided or not and changing the direction randomly
    for index,item in enumerate(ceiling_list):
        
        x_item,y_item=item.pos()
        if abs(ball.ycor()-y_item)<30 and  abs(ball.xcor()-x_item)<50:
            ceiling_list.pop(index)
            item.hideturtle()
            item.clear()
            ball.setheading(choice(set_heading))
           
#Score

score_count=turtle.Turtle()
score_count.color("white")
score_count.penup()
score_count.hideturtle()
score_count.goto(-350,280)

high_score_count=turtle.Turtle()
high_score_count.color("white")
high_score_count.penup()
high_score_count.hideturtle()
high_score_count.goto(300,280)
high_score_count.write(f"Highscore: 0",align="center",font=("Arial",12,"normal"))

def score():
    score_count.clear()
    score_count.write(f"Score:{len(score_list)-len(ceiling_list)}",align="center",font=("Arial",12,"normal"))


#Open file to check for the highscore and if the file doesn't exist it create one and save 0 as a highscore at first
def high_score():
    try:

        with open("data.txt") as score_data:
            high_score=score_data.read()
            high_score_int=int(high_score)
            return high_score_int
    except:
         with open("data.txt",mode="w") as high_data:
                high_data.write(str(0))
                return 0
    
#Compare the current score with the saved highest score and overwrite the score if the current score is higher.     
def write_score():
    current_score=len(score_list)-len(ceiling_list)
    
    if current_score > high_score():
        with open("data.txt",mode="w") as high_data:
                high_data.write(str(current_score))
            

            
        
control_paddle()
create_wall()
write_score()  

#Game on True until forever
while game_on:
    
    #Update the screen for smooth animation
    screen.update()
    score()
    collison()
    #Variable to check if the ball is falling or ascending
    before_yball=ball.ycor()

    ball.forward(ball_speed)

    #Condition to check if ball didnot collide the paddle
    if ball.ycor() < -280:
        # game_on=False
        write_score()
        high_score_saved=high_score()
        high_score_count.clear()
        high_score_count.write(f"Highscore:{high_score_saved}",align="center",font=("Arial",12,"normal"))
        ball.goto(0,0)
        ball.setheading(270)
        for ceiling in ceiling_list:
            ceiling.hideturtle()
            ceiling.clear
        ceiling_list=[]
        score_list=[]
        create_wall()

    #To check if the ball reached the top of the screen
    if ball.ycor()>280:
        ball.setheading(choice(set_heading))

    #Condition to check if the ball collided the sides and change the direction accroding to its ascend or descend
    if ball.xcor() > 380:
        if before_yball > ball.ycor(): 
            ball.setheading(225)
        else:
            ball.setheading(135)
        
    
    if ball.xcor() <-380:
        if before_yball > ball.ycor(): 
            ball.setheading(315)
        else:
            ball.setheading(45)
    

        
    
    

    
    

   
