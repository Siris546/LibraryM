class Library:
    def __init__(self,name,list):
        self.book_list = list
        self.name = name
        self.lend_books = {}

    def add_books(self, book):
        self.book_list.append(book)
        print("your book has been entered in the libarary")
        self.filewrite()

    def remove_books(self, book):
        self.book_list.remove(book)
        self.filewrite()

    def display_books(self):
        print(f"the name of the library is {self.name} and the books here are: ")
        for book in self.book_list:
            print(book)
        self.filewrite()

    def lend_book(self, user, book):
        if book not in self.lend_books.keys() and book in self.book_list:
            self.lend_books.update({book:user}) 
            print("you have succesfully lended the book, dont forget to return it by the due date")
        else:
            print(f"the book is already lended by {self.lend_books[book]}")
        self.dictwrite()
        print(f"a list of lended books: {self.dictread()}")

    def return_book(self,book):
        self.lend_books.pop(book)
        self.dictwrite()
        print("you have succesfully returned the book, thank you for returning it on time")
        self.dictread()

    def filewrite(self):
        # with open("books.txt","at") as f:
        f = open("books.txt","w")
        for book in self.book_list:
            f.write(f"{book} \n")
            # f.write('lado')
        f.close()

    def fileread(self):
        # with open("books.txt","rt") as f:
        f = open("books.txt","r")
        content = f.readlines()
        self.book_list = content
        f.close()
        return self.book_list

    def dictwrite(self):
        # with open("lend.txt","at") as f:
        f = open("lend_books.txt","w")
        for book in self.lend_books:
            f.write(f"{book}:{self.lend_books[book]}\n")

    def dictread(self):
        # with open("lend.txt","rt") as f:
        f = open("lend_books.txt", "r")
        content = f.readlines()
        for i in content:
            self.lend_books.update({i.split(":")[0]:i.split(":")[1]})
        return self.lend_books

if __name__ =="__main__":
    harry = Library("harry",["harry potter", "harry potter 2", "harry potter 3", "rich dad poor dad","2 states", "3 idiots", 'the subtle art of not giving fuck'])
    while (True):
        print("1. Display books")
        print("2. Add books")
        print("3. Lend books")
        print("4. Return books")
        print("5. Remove books")
        print("6. Exit")
        user_choice = input()
        if user_choice not in ['1','2','3','4','5','6']:
            print("please enter a valid option: ")
            continue
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            harry.display_books()
        elif user_choice == 2:
            book = input("enter the name of the book you want to add: ")
            harry.add_books(book)
        elif user_choice == 3:
            try:
                book = input("enter the name of the book you want to lend: ")
                user = input("enter your name")
                harry.lend_book(user, book)
            except Exception as e:
                print(f"{e}, please enter a valid book name")


        elif user_choice == 4:
            try:
                book = input("enter the name of the book you want to return: ")
                harry.return_book(book)
            except Exception as e:
                print(f"{e}, please enter a valid book name")

        elif user_choice == 5:
            try:
                book = input("enter the name of the book you want to remove: ")
                harry.remove_books(book)
            except Exception as e:
                print(f"{e}, please enter a valid book name to remove, this book is not in the library")

        elif user_choice == 6:
            while(user_choice!="c" or user_choice!="q"):
                print("press c to continue and q to quit")
                user_choice = input()
                if user_choice == "c":
                    break
                elif user_choice == "q":
                    exit()
                else:
                    print("please enter a valid option")
                    continue