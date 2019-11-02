import turtle

hihihi=turtle.Turtle()
turtle.setup(800,800)
turtle.bgcolor(1,0,0)

def rect():
    hihihi.fillcolor(0,0,1)    
    hihihi.begin_fill()

    for i in range(0,4):
        hihihi.forward(200)
        hihihi.right(90)
    hihihi.end_fill()

hihihi.hideturtle()
hihihi.speed(10)
hihihi.shape("turtle")
hihihi.penup()
hihihi.goto(-390,390)
hihihi.pendown()



rect()
turtle.done()
turtle.exitionclick()