import re
import emoji
from rich import print
class Library:
    def __init__(self):
        self.library_books = {
                        "10001": {"title": "A Tale of Two Cities", "author": "Charles Dickens", "available": True},
                        "10002": {"title": "Brave New World", "author": "Aldous Huxley", "available": True},
                        "10003": {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "available": True},
                        "10004": {"title": "Dune", "author": "Frank Herbert", "available": True},
                        "10005": {"title": "Emma", "author": "Jane Austen", "available": True},
                        "10006": {"title": "Frankenstein", "author": "Mary Shelley", "available": True},
                        "10007": {"title": "Great Expectations", "author": "Charles Dickens", "available": True},
                        "10008": {"title": "Hamlet", "author": "William Shakespeare", "available": True},
                        "10009": {"title": "Invisible Man", "author": "Ralph Ellison", "available": True},
                        "10010": {"title": "Jane Eyre", "author": "Charlotte Brontë", "available": True}
                    }
    def library_books_list(self):
        print(f"[bold orange]Library Books list : {emoji.emojize(':book:', language="alias")}[/bold orange]")
        print("="*40)
        for key,val in self.library_books.items():
            print(f"BOOK NUM : [bold]{key}[/bold]")
            print(f"TITLE : [bold]{val['title']}[/bold]")
            print(f"AUTHOR : [bold]{val['author']}[/bold]")
            print(f"AVAILABILITY : [bold]{val['available']}[/bold]")
            print("-"*40)
class Book(Library):
    def add_book(self,id,title,author,available):
        if id in self.library_books.keys():
                print(f"[bold red]Book ID already exits [/bold red]{emoji.emojize(':warning:')}")
                return
        self.library_books[id] = {
           "title" : title,
           "author" : author,
           "available" : available
        }
        print(f"[bold green] Book {title} added successfully {emoji.emojize(':white_check_mark:')}[/bold green]")

    def delete_book(self,id):
        if id in self.library_books.keys():
            del self.library_books[id]
            print(f"[bold green] Book with {id} deleted successfully {emoji.emojize(':white_check_mark:')}[/bold green]")
        else:
            print(f"[bold red] Book with {id} not in the list {emoji.emojize(':warning:')}")

    def update_book(self,id):
        if id in self.library_books:
            while True:
                print("[bold]Book Modification method[/bold]")
                print(f"Enter {emoji.emojize(':keycap_0:')} to exit.{emoji.emojize(':door:')}")
                print(f"Enter {emoji.emojize(':keycap_1:')} to change book name")
                print(f"Enter {emoji.emojize(':keycap_2:')} to change author name")
                print(f"Enter {emoji.emojize(':keycap_3:')} to know availability")
                try:
                    uchoice = int(input("select a book modification : "))
                    if uchoice == 1:
                        while True:
                            print(f"[bold]Previous Title = {self.library_books[id]['title']}[/bold]")
                            title = input("Enter book title : ").strip().title()
                            if not re.fullmatch(r"^[A-Za-z ]+$",title):
                                print(f"[bold red]Enter proper Book title {emoji.emojize(':cross_mark:')}")
                            else:
                                break
                        self.library_books[id]['title'] = title
                        print(f"[bold green]Book title updated to '{title}' ✅[/bold green]")
                    elif uchoice == 2:
                        while True:
                            print(f"[bold]Previous author = {self.library_books[id]['author']}[/bold]")
                            author = input("Enter author name : ").strip().title()
                            if not re.fullmatch(r"^[A-Za-z ]+$",author):
                                print(f"[bold red] Author name should contain only (a-z/ A-Z) alphabets[bold red] ")
                            else:
                                break
                        self.library_books[id]['author'] = author
                        print(f"[bold green]Book author updated to '{author}' ✅[/bold green]")
                    elif uchoice == 3:
                        while True:
                            print(f"[bold]Previous available status = {self.library_books[id]['available']}[/bold]")
                            available = input("Enter book availablility status (True/False)").strip().capitalize()
                            if available not in ["True","False"]:
                                print(f"[bold red] Available status should contain only (True/False)[/bold red]")
                            else:
                                break
                        self.library_books[id]["available"] = True if available == "True" else False
                    elif uchoice == 0:
                        print(f"[bold] Exited form Book Modification method [/bold]")
                        break
                    else:
                        print(f"[bold red]Ente proper book modification corresponding number {emoji.emojize(':warning:')}[/bold red]")
                except Exception as e:
                    print(f"[bold red]Error occurred in Book modification method{emoji.emojize(':cross_mark:')}.[/bold red]")
                    print(f"[bold red]Error : {e}[/bold red]")
        else:
            print(f"[bold red]Book {id} not found in the library[/bold red]")
b = Book()
while True:
    print("[bold]You are in BOOK class[/bold]")
    print(f"Enter {emoji.emojize(':keycap_0:')} to exit from book class")
    print(f"Enter {emoji.emojize(':keycap_1:')} to new book ")
    print(f"Enter {emoji.emojize(':keycap_2:')} to delete a book")
    print(f"Enter {emoji.emojize(':keycap_3:')} to modify book details ")
    print(f"Enter {emoji.emojize(':keycap_4:')} to view all books")
    try:
        bchoice = int(input("Select a Book class method : "))
        if bchoice == 0:
            print(f"[bold]Exited from Book class [/bold]")
            break
        elif bchoice == 1:
            print("[bold]You are in ADD BOOK method[/bold]")
            while True:
                title = input("Enter book title : ").strip().title()
                if not re.fullmatch(r"^[a-zA-Z ]+$",title):
                    print(f"[bold red]Enter proper Book TITLE [/bold red]")
                    print(f"[bold red]{title} should contain only (a-z/A-Z) letters[/bold red]")
                else:
                    break
            while True:
                last_id = next(reversed(b.library_books))
                print(f"[bold]Last book Id = {last_id}[/bold green]")
                id = input("Enter book id : ").strip()
                if not re.fullmatch(r"^[0-9]+$",id):
                    print(f"[bold red] Enter proper ID [/bold red]")
                    print(f"[bold red] {id} should contain only (0-9) Integers[/bold red]")
                else:
                    break
            while True:
                author = input("Enter book author name : ").strip()
                if not re.fullmatch(r"^[a-zA-Z ]+$",author):
                    print(f"[bold red] Enter proper AUTHOR name [/bold red]")
                    print(f"[bold red]{author} should contain only (a-z/A-Z) letters[/bold red]")
                else:
                    break
            while True:
                    available = input("Enter book availability status (True/False) : ").strip().capitalize()
                    if available not in ["True","False"]:
                        print(f"[bold red] Available status should contain only (True/False)[/bold red]")
                    else:
                        break
            availability = True if available == "True" else False
            b.add_book(id,title,author,availability)
        elif bchoice== 2:
            print("[bold] Your are Delete Book method [/bold]")
            while True:
                id = input("Enter your book id : ").strip()
                if not re.fullmatch(r"^[0-9]+$",id):
                    print(f"[bold red] Enter proper ID [/bold red]")
                    print(f"[bold red] {id} should contain only (0-9) Integers[/bold red]")
                else:
                    break
            b.delete_book(id)
        elif bchoice == 3:
            print("[bold]You are in Modify Book method [/bold]")
            while True:
                id = input("Enter your book id : ").strip()
                if not re.fullmatch(r"^[0-9]+$",id):
                    print(f"[bold red] Enter proper ID [/bold red]")
                    print(f"[bold red] {id} should contain only (0-9) Integers[/bold red]")
                else:
                    break
            b.update_book(id)
        elif bchoice == 4:
            b.library_books_list()
        else:
            print(f"[bold red]Entered method not in the Book class . {emoji.emojize(':cross_mark:')} [/bold red]")
    except Exception as e:
            print(f"[bold red]Error occurred in Book class. Error : {e}{emoji.emojize(':warning:')} [/bold red]")

# l  = Library()
# l.library_members_list()