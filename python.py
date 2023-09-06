
#--------------------------------------------------------------------------------------------------------
#imported turtle module
import turtle


wind=turtle.screen()  #initialize screen
wind.title("ping pong by doummarzz") #set the title of the window 
wind.bgcolor("black") #set the background color of the window
wind.setup(width=800,height=600) # set the width and height of the window 
wind.tracer(0)#stop the window from updating automatically


#madrab111
madrab1=turtle.Turtle()#initializes turtle object
madrab1.speed(0) #set the speed of the animation
madrab1.shape("Square")#set the shape of the ..ob
madrab1.color("blue")#set the color of the sha
madrab1.shapesize(stretch_wid=5,stretch_len=1)#streth the shape to meet the size
madrab1.penup()#stop the object from drawing line
madrab1.goto(-350,0)
#madrab22222
madrab2=turtle.turtle()
madrab2.speed(0)
madrab2.shape("Square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)
#ball
ball=turtle.turtle()
ball.speed(0)
ball.shape("Square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2.5
ball.dy=-2.5

#Function function le ha ythakam bel madrab 1 bel 2
def madrab1_up(): #get the y coordinate of the madrab
    y=madrab1.ycor()
    y+=20 #set the y increase be 20
    madrab1.sety(y)# set the y of the madrab1 to the new Y coordinate..

def madrab1_down():

   y= madrab1.ycor()
   y-=20
   madrab1.sety(y)

def madrab2_up():
    y=madrab1.ycor()
    y+=20
    madrab1.sety(y)


    def madrab2_down():
        y=madrab1.ycor()
        y-=20
madrab1.sety(y)

    #keyboard bindingsssss

wind.listen() #tell the windw to expect ke
wind.onkeypress(madrab1_up,"w")#when pressing w the func madra1_up is invoked
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"up")
wind.onkeypress(madrab2_down,"dow")

while True:
    wind.update() #update the screen everytime the loop run 


#move the ball (haded mahal ball ljdede

ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops runnn > +2.5 xaxis
ball.sety(ball.ycor() +ball.dy)#ball starts at 0 and everytime loops runnn > +2 Yaxis


#border check ,, top border +300px , bottom border -300px , ball is 20px 

if ball.ycor() > 290: #If ball is at top border
    ball.sety(290) #set y coordinate +290
#hon mn fo2 
    ball.dy *=-1 #reverse direction , making +2.50----->-2.5

if ball.ycor() <-290:
 ball.sety(290)
ball.dy*=-1  #hon mn tahet lama tdrb tabe

if ball.xcor() >390:
 ball.goto(0,0)
ball.dx *=-1

if ball.xcor() <-390:
 ball.goto(0,0) #hayde la y3ml enu tabe terj3 temro2 3al nes 
ball.dx *=-1 
