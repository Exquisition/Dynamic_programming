'''
visualizing recursion using turtle graphics


made by: Andy Zhou
Dec 29, 2018
'''




import turtle as tt # import the turtle module

window = tt.Screen()
window.bgcolor('black')
window.setworldcoordinates(-400,-400,400,1000)
tt.setup(1000,1000)  # initialize the screen object and set resolution


arrow = tt.Turtle()  # creation of turtle object saved to name 'turtle1'
arrow.left(90)
arrow.speed(0)
arrow.color('white')
arrow.fillcolor('violet')

def drawfractal(l,n):
    if (l<n):
        return
    else:
        arrow.forward(l)
        arrow.left(30)
        drawfractal(l*3/4, n)
        arrow.right(60)
        drawfractal(l *3/4, n)
        arrow.left(30)
        arrow.backward(l)

drawfractal(200, 10)

tt.mainloop()  # Pause and wait for the user to dismiss the window.






