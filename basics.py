""" 
    ------------------
    String operations
    ------------------
"""

str1 = "Hello World"
# print(str1) # Hello World
# print(str1[0]) # H

greet = str1[0:5]
name = "Hammd"
# print(greet + " " + name) # Hello Hammd 

# print(str1.upper()) # HELLO WORLD
# print(str1.lower()) # hello world
# print(len(str1)) # 11




""" 
    ------------------
    Integer operations
    ------------------
""" 
x = 20
y = 4
# print(x+y, " ", x-y, " ", x*y, " ", x/y, " ", x > y, " ", x % y) # 24 16 80 5.0 True 0



""" 
    ------------------
    List operations
    ------------------
""" 

l1 = ["dog", "cat", "fish"]

l2 = ["deer", "cow"]
l1.insert(0, l2) # [['deer', 'cow'], 'dog', 'cat', 'fish']
# print(l1[0]) # ['deer', 'cow']

l1.remove(l1[0])
l1.extend(l2) # ['dog', 'cat', 'fish', 'deer', 'cow']
l1.pop() # ['dog', 'cat', 'fish', 'deer']

l1.sort() # ['cat', 'deer', 'dog', 'fish']
l1.sort(reverse = True) # ['fish', 'dog', 'deer', 'cat']

# for i, item in enumerate(l1):
#     print(i,item)

l3 = ', '.join(l1) # fish, dog, deer, cat
l4 = l3.split(', ') # ['fish', 'dog', 'deer', 'cat']

list1 = ['A', 'B', 'C']
list2 = list1
list1[0] = 'C' # both lists are now: ['C', 'B', 'C']
x1 = {'A', 'B', 'C'}
x2 = {'B', 'A'}
# print(x1.intersection(x2)) # {'A', 'B'}
# print(x1.union(x2)) # {'C', 'A', 'B'}

#     list: []
#     tuple: ()
#     dict: {}





""" 
    ---------------------
    Dictionary operations
    ---------------------
""" 
m1 = {'food': 'pasta', 'drink': 'water'}
m2 = {'food': 'pizza', 'drink': 'juice'}
# print(m1['food']) # pasta
# print(m1.get('drink')) #water
m1['dessert'] = "cake"  # m1: {'food': 'pasta', 'drink': 'water', 'dessert': 'cake'}
del m1['dessert'] # m1: {'food': 'pasta', 'drink': 'water'}

# for key, value in m1.items():
#     print(key, value)






""" 
    --------------------
    Loops and Iterations
    --------------------
""" 
num = [1,2,3,4]
for i in num:
    i = i + 1
    #print(i)

x = 0
while True:
    if x == 5:
        break
    # print(x)
    x += 1




""" 
    ---------
    Functions
    ---------
""" 
def summation(y1, y2):
    return y1 + y2

# print(summation(278, 546))

def text(*args, **kwargs):
    print(args, kwargs)

# text('Ramen', 'Cola', dessert = 'ice cream') # ('Ramen', 'Cola') {'dessert': 'ice cream'}

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, " is a leap year")
    else:
        print(year, " is not a leap year")





""" 
    ---------
    OS Module
    ---------
""" 

import os 
# os.chdir('/Users/hammdone/Desktop')
# for dirpath, dirnames, filenames in os.walk('/Users/hammdone/Desktop'):
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()







""" 
    ------------
    File Objects
    ------------
""" 

#f = open('test.txt', 'r')  # f.name, f.mode

# with open('test.txt', 'r') as f:
#     f_contents = f.readline()
#     # print(f_contents)

# f.close()

# with open('test2.txt', 'w') as f:
#     f.write('hello')







""" 
    ----------
    CSV module
    ----------
"""
import csv

# with open('filename.csv', 'r') as f:
#     read = csv.reader(f)
#     for line in read:
#         print(line)

#     dict_read = csv.DictReader(f)
    
#     for line in dict_read:
#         print(line)

#     with open('new.txt', 'w') as new:
#         write = csv.Dictwriter(new, filenames = filenames)

#         for line in dict_read:
#             write.writerow(line)





""" 
    ----------
    CSV module
    ----------
"""
import datetime
import pytz

d1 = datetime.date.today()
d2 = datetime.date(2016, 7, 24)
delta = datetime.timedelta(days = 7) # d1 - delta
bday = datetime.date(2024, 7, 25)
seconds = (bday - d1).total_seconds()
dt = datetime.datetime(2024, 7, 3, 12, 30, 45, 100000) # 2024-07-03 12:30:45.100000
dtz = datetime.datetime.now() # 2024-07-01 22:03:07.537814+00:00
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dtz) # 2024-07-01 02:05:36.281258-06:00
format = dt_mtn.strftime('%B %d, %Y') # July 01, 2024
dt_str = 'July 01, 2024'
dt2 = datetime.datetime.strptime(dt_str, '%B %d, %Y') # 2024-07-01 00:00:00







""" 
    ----------------------------------
    Sorting Lists, Tuples, and Objects
    ----------------------------------
"""


l = [4, 8, 2, 9, 7, 0, 1, 3, 2]
t = (4, 8, 2, 9, 7, 0, 1, 3, 2)
d = {'food': 'pizza', 'drink': 'water'}

sl = sorted(l) # [0, 1, 2, 2, 3, 4, 7, 8, 9]
st = sorted(t) # [0, 1, 2, 2, 3, 4, 7, 8, 9]
sd = sorted(d) # ['drink', 'food']

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get(self):
        print("Name: ", self.name)
        print("Grade: ", self.grade)

    def __repr__(self):
        return f"Name: '{self.name}', Grade: {self.grade}"
    
s1 = Student("Bob", 68)
s2 = Student("Alice", 70)

def s_sort(student):
    return student.name

students = [s1, s2]
ss = sorted(students, key = s_sort) # [Name: 'Alice', Grade: 70, Name: 'Bob', Grade: 68]




""" 
    ---------------------------------
    Try/Except Blocks, Error Handling
    ---------------------------------
"""
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def get(self):
        print("Title: ", self.title)
        print("Pages: ", self.pages)

    def lengthy(self):
        return self.pages > 200
    
    def __repr__(self):
        return f"Book(title='{self.title}', pages={self.pages})"

b1 = Book("ABC", 402)
b2 = Book("HH", 199)

books = [b1, b2, s1]
def b_sort(book):
    return book.title

for i in books:
    try:
        if i.lengthy():
            print(i.title, "is not a lengthy book.")
        else:
            print(i.title, "is not a lengthy book.")
    except:
        print("Error")
        




""" 
    ---------------------------------
    Unit testing with unittest Module
    ---------------------------------
"""

# import unittest

# class TestBookMethods(unittest.TestCase):

#     def setUp(self):
#         self.book1 = Book("ABC", 402)
#         self.book2 = Book("HH", 199)

#     def test_lengthy_method(self):
#         self.assertEqual(self.book1.lengthy(), True)
#         self.assertEqual(self.book2.lengthy(), False)

#     def test_get_method(self):
#         self.assertEqual(self.book1.get(), "Title: ABC, Pages: 402")
#         self.assertEqual(self.book2.get(), "Title: HH, Pages: 199")

# if __name__ == '__main__':
#     unittest.main()