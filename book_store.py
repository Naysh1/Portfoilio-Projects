import random
import time

books = ["Harry Potter", "Black Holes", "Python", "Mathematics", "I am a Coder"]


def list_all_books():
    print(">>>Available books are:- ")
    for book in books:
        print(f"   * {book}")


def buy_books():
    price = random.randint(100, 201)
    x = input(">>>Enter book name: - ")
    if x in books:
        print(f"Yes,{x} is available,price of this book is {price} Rs")
        pay = int(input("Enter price of the book to pay:- \n"))
        buy = input("---Proceed (Y/n) ?")
        if buy == "Y".lower():
            if pay == price:
                print("Wait for a while payment is in process...")
                time.sleep(5)
                print("$$$ Payment Succesful $$$")
                print(
                    f"Thank you for buying {x},We hope you will like it.For more books visit our store"
                )
            books.remove(x)
        elif buy == "N".lower():
            print("Thank you for visiting our store, Have a nice day!")
        else:
            print("Enter a valid option! (Y/n)")
    else:
        print("Sorry!,This book is not available,Check the list of books")


def sell_books():
    price = random.randint(100, 201)
    print("We will give you 50% for the second hand book")
    y = input("Enter book name: - ")
    if y in books:
        print(f"Sorry we do not need {y} book,We will notify when we want.")
    else:
        print(
            f"Price of this book is {price} Rs, We will buy this book at {price/2} Rs."
        )
        sell = input("---Proceed (Y/n) ? \n  ")
        if sell == "Y".lower():
            print("Wait for a while it may take some seconds...")
            time.sleep(5)

            print(f"Congrats you sold {y} book at {price/2} Rs")
            books.append(y)
        elif sell == "N".lower():
            print("Thank you for visiting our store, Have a nice day!")
        else:
            print("Enter a valid option! (Y/n)")


welcome_msg = """*****Hello!,Welcome to the Book Store*****"""
options = """>>> Options are:--- 
    1.List all books in the Store
    2.Buy a book
    3.Sell a book
    4.Quit"""

if __name__ == "__main__":
    print(welcome_msg)
    while True:
        print(options)
        print(" ")
        x = int(input(">>>Enter Option:--- "))
        print(" ")
        if x == 1:
            list_all_books()
        elif x == 2:
            buy_books()
        elif x == 3:
            sell_books()
        elif x == 4:
            exit()
        else:
            print("Please choose a valid option!")
        print(("\n************************************************\n"))
