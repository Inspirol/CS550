import turtle, math

bob = turtle.Turtle()

jane = turtle.Turtle()



bob.color("red")

jane.color("blue")

# def spline_curve_motion(turtle: turtle.Turtle, start_pos, start_angle, end_pos, end_angle):
    
#     def spline(start_pos: tuple, start_angle, end_pos, end_angle):
#         '''
#         returns a list of points that form a spline curve based on time and the start and end points
#         '''
#         points = []
#         x0, y0 = start_pos
#         theta0 = start_angle
#         x1, y1 = end_pos
#         theta1 = end_angle
#         a = 2 * math.cos(math.radians(theta0)) + 2 * math.cos(math.radians(theta1))
#         b = 2 * math.sin(math.radians(theta0)) + 2 * math.sin(math.radians(theta1))
#         for t in range(0, 100):
#             # x(t) = (3t^2 - 2t^3)x0 + (t^3 - 2t^2 + t)a + (-3t^2 + 2t^3)x1 + (t^3 - t^2)b
#             # y(t) = (3t^2 - 2t^3)y0 + (t^3 - 2t^2 + t)c + (-3t^2 + 2t^3)y1 + (t^3 - t^2)d
            
#             x = (3 * t**2 - 2 * t**3) * x0 + (t**3 - 2 * t**2 + t) * a + (-3 * t**2 + 2 * t**3) * x1 + (t**3 - t**2) * b
#             y = (3 * t**2 - 2 * t**3) * y0 + (t**3 - 2 * t**2 + t) * a + (-3 * t**2 + 2 * t**3) * y1 + (t**3 - t**2) * b
#             theta = math.degrees(math.atan2(y, x))
#             points.append((x, y, theta))
#         return points
    
#     turtle.penup()
#     turtle.goto(start_pos)
#     turtle.setheading(start_angle)
#     turtle.pendown()
#     for point in spline(start_pos, start_angle, end_pos, end_angle):
#         turtle.goto(point[0], point[1])
#         turtle.seth(point[2])
    
    
    
    
# spline_curve_motion(bob, (0, 0), 0, (100, 100), 90)


# def spiral(turt: turtle.Turtle, cycles):
#     '''
#     recursive function that spirals outward a certain amount of cycles
#     '''
#     while turt.heading() < 360 * cycles:
#         turtle.forward(1)
#         turtle.left(1)

# spiral(bob, 2)

def tree(turtle: turtle.Turtle, branches, angle=35, length=100):
    '''
    recursive function that draws a tree
    '''
    if branches > 0:
        turtle.forward(length)
        turtle.left(angle)
        tree(turtle, branches - 1, angle * .7, length * 0.8)
        turtle.right(angle * 2)
        tree(turtle, branches - 1, angle * .7, length * 0.8)
        turtle.left(angle)
        turtle.backward(length)
        
bob.penup()
bob.setheading(90)
bob.goto(0, -200)
bob.pendown()
tree(bob, 7)

turtle.done()

