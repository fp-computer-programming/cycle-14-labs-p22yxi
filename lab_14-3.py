# Yongdong Xi
import turtle

window = turtle.Screen()
window.setup(500,500)
window.screensize(500, 500)
window.colormode(255)
window.title('Lab 3')

Zhu = turtle.Turtle()
Zhu.shape('turtle')
Zhu.pencolor(255,51,204)
Zhu.pendown()
lst = [[-200,0],[-100, 100*(3**0.5)], [0,0]]
for n in lst:
    Zhu.goto(n)


window.mainloop()
