class Rectangle:
    # 1. Initialise height and width attributes of the rectangle class
    def __init__(self, w, h):
        self.w = w
        self.h = h 
    # 2. Create the two functions for redefining the height and width
    def set_h(self, new_h): # sets height to a different value
        self.h = new_h
    
    def set_w(self, new_w): # sets the width to a different value
        self.w = new_w
        
    # 3. Create a method which calculates the area of the rectangle

quad1 = Rectangle(7, 3)
print(quad1.set_h(10))