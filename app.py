from datetime import date


# ---------- Classes ----------

class Item:
    def __init__(self, id, title, author):
        self.id, self.title, self.author = id, title, author
        self.available = True


class Book(Item):
    def __init__(self, id, title, author, subject):
        super().__init__(id, title, author)
        self.subject = subject

    def show(self):
        status = "Available" if self.available else "Issued"
        print(f"{self.id} | {self.title} | {self.author} | "
              f"{self.subject} | {status}")


class Library:
    def __init__(self):
        self.books = {}
        self.students = {}

    # 1. Search
    def search(self):
        key = input("Search: ").lower()

        result = [
            b for b in self.books.values()
            if key in b.id.lower()
            or key in b.title.lower()
            or key in b.author.lower()
            or key in b.subject.lower()
        ]

        if result:
            for b in result:
                b.show()
        else:
            print("Book not found!")

    # 2. Deposit
    def deposit(self):
        id = input("Book ID: ")

        if id in self.books:
            print("Book already exists!")
            return

        self.books[id] = Book(
            id,
            input("Title: "),
            input("Author: "),
            input("Subject: ")
        )

        print("Book deposited successfully!")

    # 3. Create Student Account
    def create_student(self):
        sid = input("Student ID: ")

        if sid in self.students:
            print("Account already exists!")
            return

        self.students[sid] = {
            "name": input("Student Name: "),
            "books": []
        }

        print("Student account created successfully!")

    # 4. Issue Book
    def issue(self):
        id = input("Book ID: ")

        if id not in self.books:
            print("Book not found!")
            return

        if not self.books[id].available:
            print("Book is already issued!")
            return

        sid = input("Student ID: ")

        if sid not in self.students:
            print("Student account not found!")
            print("Please create an account first.")
            return

        b = self.books[id]
        b.available = False
        b.student = sid
        b.taken = date.today().strftime("%d-%m-%Y")
        self.students[sid]["books"].append(id)

        print("Book issued successfully!")

    # 5. Return Book
    def return_book(self):
        id = input("Book ID: ")

        if id not in self.books:
            print("Book not found!")
            return

        b = self.books[id]

        if b.available:
            print("Book is already available!")
            return

        sid = b.student
        self.students[sid]["books"].remove(id)

        b.available = True
        del b.student
        del b.taken

        print("Book returned successfully!")

    # 6. Display Books
    def display(self):
        if not self.books:
            print("Library is empty!")
            return

        print("\nID | Title | Author | Subject | Status")
        print("-" * 70)

        for b in self.books.values():
            b.show()

    # 7. Remove Book
    def remove(self):
        id = input("Book ID: ")

        if id not in self.books:
            print("Book not found!")
            return

        if not self.books[id].available:
            print("Issued book cannot be removed!")
            return

        del self.books[id]
        print("Book removed successfully!")

    # 8. Student Details
    def student_details(self):
        sid = input("Student ID: ")

        if sid not in self.students:
            print("Student account not found!")
            return

        s = self.students[sid]

        print("\nStudent ID   :", sid)
        print("Student Name :", s["name"])
        print("Books Taken  :", len(s["books"]))

        if not s["books"]:
            print("No books currently borrowed.")
            return

        print("\nBorrowed Books:")

        for id in s["books"]:
            b = self.books[id]

            print(
                f"{b.title} | Subject: {b.subject} | "
                f"Taken: {b.taken}"
            )


# ---------- Library ----------

library = Library()

# Sample books
library.books["B001"] = Book(
    "B001", "Python Programming", "Mark Lutz", "Programming"
)

library.books["B002"] = Book(
    "B002", "Clean Code", "Robert Martin", "Software Engineering"
)

library.books["B003"] = Book(
    "B003", "Introduction to Algorithms", "Cormen", "DSA"
)


# ---------- Main Menu ----------

while True:

    print("""
========================================
       LIBRARY MANAGEMENT SYSTEM
========================================
1. Search Book
2. Deposit Book
3. Create Student Account
4. Issue / Borrow Book
5. Return Book
6. Display All Books
7. Remove Book
8. Student Borrowing Details
9. Exit
========================================
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.search()

    elif choice == "2":
        library.deposit()

    elif choice == "3":
        library.create_student()

    elif choice == "4":
        library.issue()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.display()

    elif choice == "7":
        library.remove()

    elif choice == "8":
        library.student_details()

    elif choice == "9":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice!")