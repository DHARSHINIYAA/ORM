# Ex02 Django ORM Web Application
## Date: 04.03.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<book web-1.jpg>)

## DESIGN STEPS:

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
from django.db import models
from django.contrib import admin
class lib_DB(models.Model):
    bookno=models.IntegerField(primary_key="bookno"); 
    bookname=models.CharField(max_length=50);
    author=models.CharField(max_length=20);
    genre=models.CharField(max_length=50);
    edition=models.IntegerField(max_length=5);
class lib_DBAdmin(admin.ModelAdmin):
    list_display=("bookno","bookname","author","genre","edition");
```

Include your code here

## OUTPUT

![alt text](<web 2nd exp db.jpg>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
