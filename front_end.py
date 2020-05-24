"""
With Title, Author
Year, ISBN

User options
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from backend import Database
from tkinter import *
database = Database("books.db")

class Window(object):
    def __init__(self,root):
        self.root = root

        Label_title = Label(root, text="Title")
        Label_author = Label(root, text="Author")
        Label_year = Label(root, text="Year")
        Label_isbn = Label(root, text="ISBN")

        button_0 = Button(root, text="View all", width=15, command=self.view_command)
        button_1 = Button(root, text="Search Entry", width=15, command=self.search_command)
        button_2 = Button(root, text="Add entry", width=15, command=self.insert_command)
        button_3 = Button(root, text="Update", width=15, command=self.update_command)
        button_4 = Button(root, text="Delete", width=15, command=self.delete_command)
        button_5 = Button(root, text="Close", width=15, command=quit)

        self.title_entry = Entry(root, text="")
        self.author_entry = Entry(root, text="")
        self.year_entry = Entry(root, text="")
        self.isbn_entry = Entry(root, text="")

        self.listbox = Listbox(root, height=20, width=35)
        self.listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.listbox.bind("<<ListboxSelect>> ", self.listbox_handel)

        scrollbar = Scrollbar(root)
        scrollbar.grid(column=2, row=2, rowspan=6)

        self.listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.listbox.yview)

        Label_title.grid(row=0, column=0)
        self.title_entry.grid(row=0, column=1)
        Label_author.grid(row=0, column=3)
        self.author_entry.grid(row=0, column=4)
        Label_year.grid(row=1, column=0)
        self.year_entry.grid(row=1, column=1)
        Label_isbn.grid(row=1, column=3)
        self.isbn_entry.grid(row=1, column=4)
        button_0.grid(row=2, column=3, columnspan=2)
        button_1.grid(row=3, column=3, columnspan=2)
        button_2.grid(row=4, column=3, columnspan=2)
        button_3.grid(row=5, column=3, columnspan=2)
        button_4.grid(row=6, column=3, columnspan=2)
        button_5.grid(row=7, column=3, columnspan=2)


# e.insert(0,"Enter an integer")
    def view_command(self):
        self.listbox.delete(0,END)
        for item in database.view():
            self.listbox.insert(END, item)
    def insert_command(self):

        title = self.title_entry.get()
        author = self.author_entry.get()
        year   = self.year_entry.get()
        isbn = self.isbn_entry.get()
        database.insert(title, author, year, isbn)
        self.listbox.insert(END, (title, author, year, isbn))

    def search_command(self):
        self.listbox.delete(0,END)
        title = self.title_entry.get()
        author = self.author_entry.get()
        year   = self.year_entry.get()
        isbn = self.isbn_entry.get()
        for item in database.search(title, author, year, isbn):
            self.listbox.insert(END, item)
    def delete_command(self):
        x = self.listbox.get(self.listbox.curselection())
        database.delete(x[0])
        self.view_command()
    def update_command(self):
        x= self.listbox.get(self.listbox.curselection())
        title = self.title_entry.get()
        author = self.author_entry.get()
        year   = self.year_entry.get()
        isbn = self.isbn_entry.get()
        database.update(x[0],title, author, year, isbn)
        self.view_command()

    def listbox_handel(self, hoho):
        try:
            x= self.listbox.get(self.listbox.curselection())
            id = x[0]
            title = x[1]
            author = x[2]
            year = x[3]
            isbn = x[4]
            self.title_entry.delete(0,END)
            self.author_entry.delete(0,END)
            self.year_entry.delete(0,END)
            self.isbn_entry.delete(0,END)
            self.title_entry.insert(0,title)
            self.author_entry.insert(0,author)
            self.year_entry.insert(0,str(year))
            self.isbn_entry.insert(0,str(isbn))
        except:
            pass
# text_result.grid(row= 4, column = 4)
#
# def myClick():
#     myLabel1 = Label(root, text=e.get() + " me", background = "#000fff000")
#     myLabel1.pack()
# myLabel2 = Label(root, text = "My name is what the fuck \n LOLO ")
root = Tk()
root.title("database")
Window(root)
root.mainloop()
