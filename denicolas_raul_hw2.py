import turtle
s = turtle.getscreen()
t = turtle.Turtle()

turtle.bgcolor("Burlywood")

turtle.title("My Turtle Picture")

t.pensize(5)


t.fillcolor("Burlywood")
t.pencolor("DarkGoldenrod")


t.penup()
t.lt(90)
t.lt(90)
t.fd(50)
t.lt(90)
t.lt(90)
t.pendown()

#House Frame
t.begin_fill()
t.fd(100)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(150)
t.end_fill()

#Doorframr
t.begin_fill()
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(50)
t.end_fill()

t.lt(90)
t.lt(90)
t.fd(150)
t.rt(45)

#Roof
t.begin_fill()
t.fd(74)
t.rt(90)
t.fd(74)
t.end_fill()

#Chimmney
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.lt(135)
t.fd(35)
t.lt(90)
t.fd(15)
t.lt(90)
t.fd(35)
t.lt(90)
t.fd(15)
t.end_fill()

#Window
t.pencolor("DarkGoldenrod")
t.penup()
t.bk(4)
t.rt(90)
t.fd(6)
t.fd(20)
t.pendown()
t.rt(90)
t.fd(40)
t.lt(90)
t.fd(40)
t.lt(90)
t.fd(40)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(40)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(40)

#Window 2
t.penup()
t.lt(90)
t.fd(55)
t.lt(90)
t.fd(20)
t.pendown()
t.fd(25)
t.rt(90)
t.fd(25)
t.penup()
t.rt(90)
t.fd(25)
t.pendown()
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(12)
t.rt(90)
t.fd(25)

t.penup()
t.lt(90)
t.fd(90)
t.lt(90)

t.pendown()
t.fd(25)
t.lt(90)
t.fd(47)
t.penup()

t.bk(47)
t.rt(90)
t.fd(75)

t.lt(45)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.fd(150)

t.lt(45)
t.fd(140)

t.lt(135)
t.fd(150)
t.bk(150)
t.end_fill()

t.rt(90)
t.fd(75)


t.lt(90)
t.fd(150)

t.lt(45)
t.fd(45)
