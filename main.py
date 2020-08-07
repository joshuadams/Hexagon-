import turtle
hexa = turtle.Turtle()

def createHexagon(col, size, x, y):
  hexa.color(col)
  for i in range(6):
    hexa.forward(100)
    hexa.right(60)

createHexagon('red', 100, 100, 100)
