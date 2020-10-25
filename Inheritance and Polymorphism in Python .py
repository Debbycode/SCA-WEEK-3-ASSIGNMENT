#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Books:

    def __init__(self, Title, Author):
        self.__Title = Title      # __name is private to Vehicle class
        self.__Author = Author

    def getAuthor(self):         # getColor() function is accessible to class Car
        return self.__Author

    def setAuthor(self, Author):  # setColor is accessible outside the class
        self.__Author = Author

    def getTitle(self):          # getName() is accessible outside the class
        return self.__Title

class Genre(Books):

    def __init__(self, Title, Author, Year_published):
        # call parent constructor to set name and color  
        super().__init__(Title, Author)       
        self.__Year_published = Year_published

    def getDescription(self):
        return self.getTitle() + self.__Year_published + " in " + self.getAuthor() + " Author"

# in method getDescrition we are able to call getName(), getColor() because they are 
# accessible to child class through inheritance

c = Genre("Think Big", "Ben Carson", "1990")
print(c.getDescription())
print(c.getTitle()) # car has no method getName() but it is accessible through class Vehicle


# In[ ]:





# In[7]:





# In[ ]:





# In[ ]:




