import turtle

# Recursive function to draw the tree
def draw_tree(branch_length, left_angle, right_angle, reduction_factor, depth):
    if depth == 0 or branch_length < 1:
        return
# Set color and thickness by depth
    turtle.pensize(depth)
    if depth <= 2:
        turtle.color("forest green")
    else:
        turtle.color("saddle brown")
        
    turtle.forward(branch_length)
    
    # Save current state
    current_position = turtle.position()
    current_heading = turtle.heading()

    # Left branch
    turtle.left(left_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1)

    # Restore state
    turtle.penup()
    turtle.setposition(current_position)
    turtle.setheading(current_heading)
    turtle.pendown()

    # Right branch
    turtle.right(right_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1)

    # Restore again
    turtle.penup()
    turtle.setposition(current_position)
    turtle.setheading(current_heading)
    turtle.pendown()


# Get user input
left_angle = float(input("Enter left branch angle (in degrees): "))
right_angle = float(input("Enter right branch angle (in degrees): "))
start_length = float(input("Enter starting branch length (in pixels): "))
reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))
depth = int(input("Enter recursion depth: "))

# Setup turtle
turtle.speed("fastest")
turtle.left(90)
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()

# Draw the tree
draw_tree(start_length, left_angle, right_angle, reduction_factor, depth)

turtle.done()
