#!/usr/bin/env python
# coding: utf-8

# In[35]:


import sqlite3

connection = sqlite3.connect("bookstore.db")
print ("====================")
print("Connection Succesful!")
print ("====================")


# In[36]:


cursor = connection.cursor()
cursor.execute("CREATE TABLE books (Title TEXT, Author TEXT, Genre TEXT, Shelf_number INTEGER)")

print ("=============")
print("Table Created!")
print ("=============")


# In[37]:


cursor.execute("INSERT INTO books VALUES ('Purple Hibiscus', 'Chimamanda Ngozi Adichie', 'Fiction Novel', 616)") 
cursor.execute("INSERT INTO books VALUES ('Developing the Leader in You', 'John C. Maxwell', 'Motivational & Inspirational', 134)")
cursor.execute("INSERT INTO books VALUES ('Circe', 'Madeline Miller', 'Fantasy', 620)")
cursor.execute("INSERT INTO books VALUES ('The boy, the Mole, the Fox and the Horse', 'Charlie Mackery', 'Comic', 320)")
cursor.execute("INSERT INTO books VALUES ('The testmants', 'Margeret Atwood', 'Science Fiction', 192)")
cursor.execute("INSERT INTO books VALUES ('I know why the Caged Bird Sings', 'Maya Angelou', 'Biographies & Autobiographies', 209)")
cursor.execute("INSERT INTO books VALUES ('Think Big', 'Ben Carson', 'Motivational & Inspirational', 134)")
cursor.execute("INSERT INTO books VALUES ('1984', 'Gorge Orwell', 'Science Fiction', 192)")

print ("=============")
print("Data Inserted!")
print ("=============")


# In[38]:


rows = cursor.execute("SELECT Title, Author, Genre, Shelf_number FROM books").fetchall()
rows


# In[39]:


#To retrieve values for the each columns in the books table,
#the SELECT statement is used

target_books_Title = "Think Big"
rows = cursor.execute(
    "SELECT Title, Author, Genre, Shelf_number FROM books WHERE Title = ?",
    (target_books_Title,),
).fetchall()
print(rows)


# In[40]:


# A book has been moved from a shelf to a new shelf and now has a new shelf number
# The UPDATE statement is used to make this changes

new_shelf_number = 710
moved_books_genre = "Comic"
cursor.execute(
    "UPDATE books SET Shelf_number = ? WHERE genre = ?",
    (new_shelf_number, moved_books_genre)
)

print ("===================================================")
print(str(moved_books_genre)+" "+"Books"+" "+"Succesfully Change Shelf Number to"+" "+str(new_shelf_number)+"!")
print ("===================================================")


# In[41]:


rows = cursor.execute("SELECT Title, Author, Genre, Shelf_number FROM books").fetchall()
rows


# In[42]:


#A book has been sold out and no longer in stock
#The DELETE SQL statement is used to remove the sold book from table 

sold_books = "Purple Hibiscus"
cursor.execute(
    "DELETE FROM books WHERE Title = ?",
    (sold_books,)
)

print ("======================================")
print(str(sold_books)+" "+"no longer in Stock!")
print ("======================================")


# In[43]:


rows = cursor.execute("SELECT Title, Author, Genre, Shelf_number FROM books").fetchall()
rows


# In[44]:


#Close connection and Cursor
#The WITH SQL statement is used

from contextlib import closing

with closing(sqlite3.connect("bookstore.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("select 1").fetchall()
       
        
print ("====================")
print("Connection Closed!")
print ("====================")


# In[ ]:





# In[ ]:




