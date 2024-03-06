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

