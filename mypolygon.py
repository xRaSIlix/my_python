import turtle
bob = turtle.Turtle()
print(bob)
bob.lt(135)
for i in range (50):
    bob.fd(100)
    bob.rt(90)
    bob.fd(50)
    bob.lt(90)
    bob.fd(100)
    bob.rt(90)

turtle.mainloop()