import turtle

t = turtle.Turtle()
t.shape("turtle")

size = 20

for i in range(30): #30번 반복
    size +=3
    t.forward(size)
    t.right(24)
    
