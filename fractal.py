import random
import turtle

def draw_fractal(length, depth):
  if depth == 0:
    return
  
  # Generate a random color
  color = random.choice(["blue", "red", "green", "yellow", "purple", "orange"])
  turtle.color(color)

  # Draw a circle with the given length
  turtle.circle(length)
  
  # Turn the turtle left by 90 degrees
  turtle.left(90)
  
  # Draw another circle with the given length
  turtle.circle(length)
  
  # Turn the turtle right by 180 degrees
  turtle.right(180)
  
  # Draw another circle with the given length
  turtle.circle(length)
  
  # Turn the turtle left by 90 degrees
  turtle.left(90)
  
  # Recursively draw the fractal with reduced length and increased depth
  draw_fractal(length * random.uniform(0.2, 5), depth-1)
  
# Set turtle screen updates to happen immediately
turtle.tracer(0, 0)

# Set the turtle window's background color
turtle.bgcolor("black")

# Start drawing the fractal with a length of 100 and a depth of 50
draw_fractal(100, 50)

# Hide the turtle cursor
turtle.hideturtle()

# Keep the window open until it is closed
turtle.mainloop()
