#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Python program that create a class triangle and define two methods, create_triangle() and print_sides().

# In[1]:


class triangle:
    def create_triangle(self):
        print('create_triangle')

    def print_sides(self):
        print('print sides')


# ## 2. Write a Python program to create a class with two methods get_String() and print_String().

# In[2]:


class xyz:
    def get_string(self):
        print('get_string')
        
    def print_string(self):
        print('print_string')


# ## 3. Write a Python program to create a class Rectangle that takes the parameter length and width. The class should also contain a method for computing its perimeter.

# In[3]:


class Rectangle:
    def _init_(self,length,width):
        self.length = length
        self.width = width
        
    def perimeter(self):
        return 2 * (self.length + self.width)


# ## 4.  Write a Python program to create a class Circle that takes the parameter radius. The class should also contain two methods for computing its area & perimeter respectively. Use constructor to implement initialization of parameters.

# In[4]:


class circle:
    def _init_(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius


# ## 5.Create a Circle class and initialize it with radius. Make two methods get Area and get Circumference inside this class.

# In[9]:


class circle:
    def _init_(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius


# ## 6. Create a Temperature class. Make two methods:
# ##### a)	Convert Fahrenheit - It will take Celsius and will print it into Fahrenheit.
# ##### b)	Convert Celsius - It will take Fahrenheit and will convert it into Celsius.

# In[ ]:


class temperature:
    def fahrenhiet(self):
        return (9 * cel)/5 + 32
    
    def convertCelsius(self,fah):
        return (5 * fah)/9 - 32


# ## 7. Create a Student class and initialize it with name and roll number. Make methods to:
# ##### 1. Display - It should display all information’s of the student.
# ##### 2. SetAge - It should assign age to student.
# ##### 3. SetMarks - It should assign marks to the student.

# In[19]:


class student:
    def basic_profile(self):
        return (self.name,self.rollno, self.marks,self.age)
    
stu1=Student()
stu1.name="Madhur"
stu1.rollno="2k20CSUN03005"
stu1.marks=90
stu1.age= 18
print(stu1.basic_profile())


# ## 8. Write a Python class to reverse a string word by word.

# In[11]:


class reverse_String:
    def reverse(self,string):
        word = ""
        sentence_list = []
        for x in range(0,len(string)):
            if string[x] == ' ':
                sentence_list.append(word)
                word = ""
            else:
                word = word + string[x]
        
        for x in range(0,len(sentence_list)):
            word = word + ' ' + sentence_list[x]
        
        print(word)


# In[ ]:




