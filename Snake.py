import turtle as t 
import random
import time

delay = 0.1
score=0
highscore=0

wn= t.Screen()
wn.title(" Snake Game ")
wn.bgcolor("green")
wn.setup(width=.75,height=.75)
wn.tracer(0)


head=t.Turtle()
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.speed(0)
head.direction='stop'


food=t.Turtle()
food.shape("circle")
food.color("red")
food.penup()
x=random.randint(-500,500)
y=random.randint(-300,300)
food.goto(x,y)
food.speed(0)

segments=[]

pan=t.Turtle()
pan.shape("square")
pan.color("white")
pan.penup()
pan.hideturtle()
pan.goto(0,270)
pan.write("Score: 0   Highscore: 0  ",align="center",font=("Ariel",24,"normal"))

def gameover():
    global score,highscore
    for i in segments:
        i.goto(5000,5000)
    segments.clear()
    head.goto(0,0)
    head.direction='stop'
    score=0
    pan.clear()
    pan.write("Score: 0   Highscore: {}  ".format(highscore),align="center",font=("Ariel",24,"normal"))
        


def go_up():
    if head.direction != 'down':
        head.direction='up'

def go_down():
    if head.direction != 'up':
        head.direction='down'

def go_right():
    if head.direction != 'left':
        head.direction='right'

def go_left():
    if head.direction != 'right':
        head.direction='left'



def move():

    if head.direction == 'up':
        y=head.ycor()
        head.sety(y+20)
    
    if head.direction == 'down':
        y=head.ycor()
        head.sety(y-20)
    
    if head.direction == 'right':
        x=head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x=head.xcor()
        head.setx(x-20)


wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_right,'d')
wn.onkeypress(go_left,'a')


while True:
    wn.update()
    
    if head.xcor() > 500 or head.xcor() < -500 or head.ycor()>300 or head.ycor() < -300:
        gameover()
        time.sleep(0.1)



    if head.distance(food) < 20:
        x=random.randint(-500,500)
        y=random.randint(-300,300)
        food.goto(x,y)
        tail=t.Turtle()
        tail.shape("square")
        tail.color("skyblue")
        tail.speed(0)
        tail.penup()
        segments.append(tail)

        score+=1
        if(score>highscore):
            highscore=score
        
        pan.clear()
        pan.write("Score: {}   Highscore: {}  ".format(score,highscore),align="center",font=("Ariel",24,"normal"))

        delay-=0.001
       
       

          
    #arrange the segments in inverse order
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    for i in segments:
        if i.distance(head)<20:
            gameover()
            time.sleep(0.1)

    time.sleep(delay)


wn=t.mainloop()