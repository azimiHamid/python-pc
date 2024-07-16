class Point:
    # constructor function
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print("Draw")
        
    def move(self):
        print("Move")


# creat object from class
point_1 = Point(5, 7)
point_2 = Point(y=18.1, x=45.3)

# modify attributes
point_1.x = 9

print(point_1.x)
print(point_1.y)

print(point_2.x)
print(point_2.y)

# call methods of the class instance/object
point_1.move()
point_1.draw()
