class Books:
    def __init__(self, author, title, price, publisher, stock_position):
        self.author = author
        self.title = title
        self.price = price
        self.publisher = publisher
        self.stock_position = stock_position
    
def search(books, title, author):
    for i in books:
        if (i.title == title and i.author == author):
            print(f'Book Name: {i.title}')
            print(f'Author: {i.author}')
            print(f'Book Price: {i.price}')
            print(f'Book Publisher: {i.publisher}')
            print(f'Available copies: {i.stock_position}')
            n = int(input("Enter number of copies required: "))
            if n <= i.stock_position:
                print(f'Total price: {i.price * n}')
                return
            else:
                print("Insufficient copies")
                return
    print("Not Available")

b1 = Books("Ralph", "garage", 120, "Winnie Gardner", 42)
b2 = Books("Amanda", "teach", 216, "Ruby Potter", 14)
b3 = Books("Ida", "bright", 391, "Myrtle Morris", 19)
b4 = Books("Mason", "party", 406, "Helena Stephens", 6)
b5 = Books("Lottie", "atomic", 457, "Henry Lambert", 6)

lib = [b1, b2, b3, b4, b5]
title = input("Title: ")
author = input("Author: ")
search(lib, title, author)