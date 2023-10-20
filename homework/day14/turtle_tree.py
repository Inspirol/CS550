import turtle

bob = turtle.Turtle()

def tree(turtle: turtle.Turtle, branches, angle=35, length=100):
    '''
    recursive function that draws a tree
    
    :param turtle: the turtle object that draws the tree
    
    :param branches: the number/level of branches the tree has
    
    :param angle: the initial angle of the branches
    
    :param length: the initial length of the branches
    '''
    if branches > 0:
        turtle.forward(length)
        turtle.left(angle)
        # recursive call that reduces the length and angle, and reduces the number of branch levels
        tree(turtle, branches - 1, angle * .7, length * 0.8)
        # moving to the other side of the tree branch
        turtle.right(angle * 2)
        # same recursive call as before
        tree(turtle, branches - 1, angle * .7, length * 0.8)
        turtle.left(angle)
        # moving back to the original position
        turtle.backward(length)
        
bob.penup()
bob.setheading(90)
# moving the turtle to the bottom of the screen to give space for the tree
bob.goto(0, -200)
bob.pendown()
tree(bob, 7)

turtle.done()
