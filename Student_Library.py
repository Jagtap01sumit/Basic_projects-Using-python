from operator import truediv


class Library:
    def __init__(self,List_of_Books):
        self.books=List_of_Books

    def display_Available_Books(self):
        print("The Available Books In Library Are:")
        for book in self.books:
            print("*"+book)

    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please return this books in 30 days!!")
            self.books.remove(bookname)
            return True
        else:
            print(f"Sorry {bookname} is not available in Libraray, please wait until the books is returned!!")
            return False
    def returnBook(self,bookname):
        self.books.append(bookname)
        print(f"Thanks for returning {bookname} book !, hope you enjoyning reading")


class Student:
    def requestBook(self):
        self.book=input("Enter the book name you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book=input("Enter the book name you want to return: ")
        return self.book



if __name__=="__main__":
    centralLibrary=Library(["java","python","c++","flask","AI"])
    student=Student()

    while(True):
        print(''' *****Welcome to Central Library*****
        please chose an option:
        1. Listing of all books
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        ''')
        a=int(input("Enter the choise: "))
        if a==1:
            centralLibrary.display_Available_Books()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Central Library, have a great day!!")
            exit()
        else:
            print("Invalid choise")

        
