class Rectangle:
    
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    

    def __lt__(self,other):
        area1 = self.__length * self.__width
        area2 = other.__length * other.__width

        if area2 < area1:
            print("Rectangle 1 is Larger")
        elif area1 < area2:
            print("Rectangle 2 is Larger")

        else:
            print("Both rectangles are equal")
         



length1=int(input("enter the length:"))
width1=int(input("enter the width:"))


length2=int(input("enter the length:"))
width2=int(input("enter the width:"))


rect1=Rectangle(length1,width1)
rect2=Rectangle(length2,width2)

rect1 < rect2
