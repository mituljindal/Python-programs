import turtle

#define draw_square functiom
def draw_square(pointer):
    for j in range(0,4):
        pointer.forward(100) #move the turtle foward by 100
        pointer.right(90) #turn the turle right by 90 degrees
    
#define the draw function
def draw_art():
    window = turtle.Screen() #open a screen to draw
    window.bgcolor("green") #give the screen color
    
    pointer = turtle.Turtle() #initiate a pointer
    pointer.shape("turtle") #give the pointer a shape
    pointer.color("dark blue") #give the pointer a color
    pointer.speed(0) #set pointer speed

    #make a circle out of squares
    n = 120
    for i in range(0,n):
        draw_square(pointer) #draw square          
        pointer.right(360/n) #turn the turtle 5 degrees for next square
    
    window.exitonclick() #click the screen to exit

draw_art()
