from graphics import *
# win = GraphWin('Shapes')
# center = Point(100, 100)
# circ = Circle(center, 30)
# circ.setFill('red')
# circ.draw(win)
# label = Text(center, "Red Circle")
# label.draw(win)
# rect = Rectangle(Point(30, 30), Point(70, 70))
# rect.draw(win)
# line = Line(Point(20, 30), Point(180, 165))
# line.draw(win)
# oval = Oval(Point(20, 150), Point(180, 199))
# oval.draw(win)

# win=GraphWin("Click me!")
# p=win.getMouse()
# print("You clicked (x,y)=(", p.getX(),",",p.getY(),")")


# triangle.pyw
# Interactive graphics program to draw a triangle
# from graphics import *
#def main():
win = GraphWin("Draw a Triangle")
win.setCoords(0.0, 0.0, 10.0, 10.0)
message = Text(Point(5, 0.5), "Click on three points")
message.draw(win)
# Get and draw three vertices of triangle
p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
p2.draw(win)
p3 = win.getMouse()
p3.draw(win)
# Use Polygon object to draw the triangle  
triangle = Polygon(p1,p2,p3)  
triangle.setFill("peachpuff")  
triangle.setOutline("cyan")  
triangle.draw(win)

# Wait for another click to exit  message.setText("Click anywhere to quit.")  win.getMouse()




