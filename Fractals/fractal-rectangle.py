import turtle

obj = turtle.Turtle()
obj.left(90)
obj.backward(300)
obj.speed(100)
obj.right(30)
obj.clear()

def draw(l):
    if(l<5):
        return
    else:
        obj.forward(l)
        obj.left(60)
        draw_1(l / 2.2)
        obj.forward(l)
        obj.left(120)
        draw(l / 2.2)
        obj.forward(l)
        obj.left(60)
        draw_1(l / 2.2)
        obj.forward(l)
        obj.left(120)
        draw(l / 2.2)

def draw_1(l):
    if(l<5):
        return
    else:
        obj.forward(l)
        obj.left(120)
        draw(l / 2.2)
        obj.forward(l)
        obj.left(60)
        draw_1(l / 2.2)
        obj.forward(l)
        obj.left(120)
        draw(l / 2.2)
        obj.forward(l)
        obj.left(60)
        draw_1(l / 2.2)

draw(300)
input()