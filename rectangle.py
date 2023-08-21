## Turtles project
## Nicholas Ngobi
## Monday,August 21
import turtle
turtle.color("green")
turtle.speed(1)
def rectangle(length, height):
    for i in range (0,4):
        if i%2==0:
           turtle.forward(length)
           turtle.right(90)
        else:
            turtle.forward(height)
            turtle.right(90)

def polygon(size,n):
    for  i in range(1,9):
        
        turtle.forward(size)
        turtle.left(45)

def stop(length,height,size,n):

#def move(length,n):
    #turtle.forward(length/2)
    polygon(size,n)
    rectangle(length,height)
def triangle(size):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
def house(size):
    triangle(size)
    square(size)

def main():
    #polygon(50,8)
    #rectangle(10,100)
    stop(10,150,50,8)
    #triangle(100)
    #square(100)
    #house(100)
    turtle.Screen().exitonclick()
main()
