# Yongdong Xi
import turtle

window = turtle.Screen()
window.setup()
window.screensize()
window.colormode(255)
window.title('Lab 4')

Diao = turtle.Turtle()
Diao.shape('turtle')
Diao.speed(2)
Diao.pencolor(0,255,0)
Diao.pendown
Diao.stamp()
Diao.fillcolor(203,255,51)
Diao.begin_fill()
Diao.goto(100,0)
Diao.goto(100,-100)
Diao.goto(0,-100)
Diao.goto(0,0)
Diao.end_fill()
window.exitonclick()
window.mainloop()