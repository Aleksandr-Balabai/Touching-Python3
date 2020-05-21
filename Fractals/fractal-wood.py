import turtle

obj = turtle.Turtle()
obj.left(90)
obj.backward(300)
obj.speed(100)
obj.clear()
def draw(l):
    if(l<4):
        return
    else:
        obj.forward(l)
        obj.left(60)
        draw(l/2)
        obj.right(30)
        draw(l/2)
        obj.right(30)
        draw(l/2)
        obj.right(30)
        draw(l/2)
        obj.right(30)
        draw(l/2)
        obj.left(60)
        obj.backward(l)


draw(400)
input()