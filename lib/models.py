from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



# Create your models here.
class Categories(models.Model):
    choices = [
        ('science', 'Science'),
        ('history', 'History'),
        ('biography', 'Biography'),
        ('literature', 'Literature'),
        ('law', 'Law'),
    ]
    
    category = models.CharField(max_length=30, choices=choices, default='science')

    def __str__(self):
        return str(self.category)



class book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    isbn = models.PositiveBigIntegerField()
    author = models.CharField(max_length=30, null=True, blank=True)
    category = models.ForeignKey(Categories, null=True, blank=True,on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'media')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return (self.title) + str([self.isbn])

