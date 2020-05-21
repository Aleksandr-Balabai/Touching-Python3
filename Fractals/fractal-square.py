import turtle

obj = turtle.Turtle()
obj.speed(100)
obj.backward(300)
obj.left(90)
obj.backward(300)
obj.right(90)
obj.clear()

def draw(l):
    if(l<3):
        return
    else:
        obj.forward(l)
        obj.left(90)
        draw(l / 2.5)
        obj.forward(l)
        obj.left(90)
        draw(l / 2.5)
        obj.forward(l)
        obj.left(90)
        draw(l / 2.5)
        obj.forward(l)
        obj.left(90)
        draw(l / 2.5)

draw(700)
input()