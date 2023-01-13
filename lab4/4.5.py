class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("**************BOOK DETAILS******************\n")
        print("Publisher's Name: ",self.name)

        
class Book(Publisher):
    def __init__(self,name,title,author):
        self.title=title
        self.author=author
        super().__init__(name)
    def display(self):
        super().display()
        print("Title of the book: ",self.title)
        print("Author of the book: ",self.author)


class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        self.price=price
        self.no_of_pages=no_of_pages
        super().__init__(name,title,author)

    def display(self):
        super().display()
        print("Price of the book: ",self.price)
        print("Number of pages: ",self.no_of_pages)

        
name=input("Enter the Publisher name:")
title=input("Enter the Book's title:")
author=input("Enter the Author's name")
price=int(input("Enter the Price of the book:"))
no_of_pages=int(input("Enter the number of pages:"))

obj=Python(name,title,author,price,no_of_pages)
obj.display()
