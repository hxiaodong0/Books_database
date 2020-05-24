import sqlite3

class Database():
   def __init__(self,db):    #Object we want to perform; object instances;; __init__ will be excuted when the class is called
      self.conn = sqlite3.connect(db)
      self.cur = self.conn.cursor()  # create cursor
      self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer )")
      self.conn.commit()  # commit
   # create a seperated function to add item to the database

   def insert(self,title ="/NA", author="/NA", year="/NA", isbn="/NA"):
      # cur.execute("INSERT INTO book VALUES ('%s','%s','%s') "%(title, author, year, isbn))      #sql injection attacks
      self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
      self.conn.commit()  # commit

   def view(self):
      #cur.execute("INSERT INTO store VALUES ('%s','%s','%s') "%(item, quantity, price))      #sql injection attacks
      self.cur.execute("SELECT * FROM book")
      rows = self.cur.fetchall()
      return rows

   def search(self, title="", author = "", year="", isbn=""):    #default ="" to handel error;;;
      self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title,author,year, isbn))  # comma to make your parameters a tuple:
      rows = self.cur.fetchall()
      self.conn.commit()
      return rows

   def delete(self, id):

      self.cur.execute("DELETE FROM book WHERE id = ?", (id,))  # comma to make your parameters a tuple:
      self.conn.commit()
      # self.cur.close()

   def update(self, id,title, author, year, isbn):
      self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))  # comma to make your parameters a tuple:
      self.conn.commit()

# __del__ is a finalizer. It is called when an object is garbage collected which happens at some point after all references to the object have been deleted.
   def __del__(self): # Before the script is exited.
      self.conn.close()
      print("__del__ function is called")

if __name__ == "__main__":    # When this file is excuted on itself, excute; otherwise, don't perform this
   pass



# print(view())
# insert("nothing later on")

# insert("what the fuck", "Xiaodong", 2020,15811461245)
# print(view())
# print("search result:", search(author= "Xiaodong"))
# insert('hold shit',"Eric", 123 , 787827187281787281)
# update(2, 'hold shit',"Eric","02010021","787827187281787281")
# print(view())
