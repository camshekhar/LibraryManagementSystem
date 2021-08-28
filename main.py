class Library:
    def __init__(self, listOfbooks):
        self.books = listOfbooks

    def displayAvailableBooks(self):
        print("\nBooks Available in this Library are:\n")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} book. Please keep it safe and return it on time.")        
            self.books.remove(bookName)
            return True
        else:
            if len(bookName)!=0:
                print(f"This {bookName} book has already been issued to someone or may not be availble.")
            else:
                print("\nPlease enter a Valid Book Name.\n")    
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Your book has been returned successfully.")
         

class Student:
    def requestBook(self):
        self.book = input("Enter Name of a book to issue: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter Name of a book to return: ")
        return self.book


if __name__ == '__main__':
    Central_Library = Library(['Algorithms','Python','Django','HTML','CSS'])
    student = Student()

    while(True):
        welcomeMsg = ''' ======= Welcome to Central Library =======
        PLease Choose an Option below:
        1. List All Books
        2. Request a Book
        3. Add/Return a Book
        4. Exit from Library
        '''
        print(welcomeMsg)
        a = int(input("Enter Your Choice:\n"))
        if a == 1:
            Central_Library.displayAvailableBooks()
        elif a == 2:
            Central_Library.borrowBook(student.requestBook())
        elif a == 3:
            Central_Library.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks! for Using this Central Library.")
            exit()
        else:
            print("Invalid Choice!")    


        