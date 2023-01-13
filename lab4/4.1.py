class Rectangle():
    def __init__(self,l1,b1):
        self.length=l1
        self.breadth=b1
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)


l1=int(input("Enter the length of rectangle1:"))
b1=int(input("Enter the breadth of rectangle1:"))
l2=int(input("Enter the length of rectangle2:"))
b2=int(input("Enter the breadth of rectangle2:"))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
if rect1.area() > rect2.area():
    print(" The first Rectangle is bigger")
else:
    print(" The second Rectangle is bigger")
