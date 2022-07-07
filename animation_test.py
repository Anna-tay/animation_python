import turtle
import time 

window = turtle.Screen()

window.title("Animation Flower")
window.bgcolor("black")

player = turtle.Turtle()
player.shape("square")
player.color("green")

while True:
    player.shape("square")
    time.sleep(0.5)
    player.shape("circle")
    time.sleep(0.5)


window.mainloop()