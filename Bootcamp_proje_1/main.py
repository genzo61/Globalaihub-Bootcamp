class Library:
    def __init__(self):
        try:
            self.file = open("books.txt", "a+")
        except IOError:
            print("Error: Unable to open or create the file 'books.txt'.")
            self.file = None

    def __del__(self):
        if hasattr(self, 'file'):
            self.file.close()
    def list_books(self):
        if self.file is not None and not self.file.closed:
            self.file.seek(0)
            file = open("book.txt","r")
            book_lines = self.file.read().splitlines()
            for line in book_lines:
                book_info = line.split(',')
                if len(book_info) == 2:
                    book_name,auothor = book_info
                    print(f" Book: {book_name}, Author: {auothor}")
                else:
                    print("there is no information about your book and authors")
        else:
            print("there is no error")
    def add_book(self):
        if self.file is not None and not self.file.closed:
            book_title = input("Enter book title")
            book_author = input("Enter book author")
            num_pages = int(input("enter number of pages"))
            first_rel_year = int(input("enter first release year"))
            book_info = f"Book Title: {book_title},Book Author: {book_author},Number of pages: {num_pages},First Release Year: {first_rel_year}"
            with open("books.txt", "a+") as f:
                f.write(book_info)
            print("book added in file")
        else:
            print("no error")
    def remove_book(self):
        if self.file is not None and not self.file.closed:
            book_title_to_remove = input("Enter book title which is you want to delete")
            self.file.seek(0)
            book_lines = self.file.read().splitlines()
            updated_book_lines = []
            for line in book_lines:
                book_info = line.split(",")
                if len(book_info) == 4 and book_info[0] == book_title_to_remove:
                    print(f"{book_title_to_remove} is removed...")
                else:
                    updated_book_lines.append(line)
            self.file.seek(0)
            self.file.truncate()
            for line in updated_book_lines:
                self.file.write(line + "\n")
        else:
            print("no error")



def menu():
    lib = Library()
    if lib.file is None:
        return
    while 1:
        print("*************** MENU **************")
        print(" 1) List Books")
        print(" 2) Add Books")
        print(" 3) Remove Books")
        islem = input("Enter what yo want to do")
        if(islem == "1"):
            lib.list_books()
        elif(islem == "2"):
            lib.add_book()
        elif(islem == "3"):
            lib.remove_book()
        else:
            print("please enter valid process in the menu")
            break

if __name__ == "__main__":
    menu()