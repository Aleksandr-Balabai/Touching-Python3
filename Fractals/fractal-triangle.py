import turtle

obj = turtle.Turtle()
obj.speed(100)
obj.backward(300)
obj.left(90)
obj.backward(300)
obj.right(90)
obj.clear()

def draw(l):
    if(l<4):
        return
    else:
        obj.forward(l)
        obj.left(120)
        draw(l / 2)
        obj.forward(l)
        obj.left(120)
        draw(l / 2)
        obj.forward(l)
        obj.left(120)
        draw(l / 2)


draw(800)
input()