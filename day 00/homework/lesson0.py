from turtle import *

#we want to pain a house

# step 1:draw a square
begin_fill()
speed(30)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
    
forward(200)
left(90) 
end_fill()
#end of square

#drawoing a doorforward
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill() #end of drawing door

penup()
goto(40, 80)
color ("light grey")

right(60)
pendown()
begin_fill()
forward(30)
right(90)
forward(30)  
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(150,80)
pendown()
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()
penup()



color("brown")


goto(-100, 100)

pendown()

forward(100)

begin_fill()

# the trees leafts:)





right(90)
forward(30)
right(90)
forward(100)
right(90)
forward(30)

end_fill()

color("green")
begin_fill()
forward(30)
left(90)
forward(60)
left(90)
forward(90)
left(90)
forward(60)
left(90)
forward(30)

end_fill()


exitonclick()