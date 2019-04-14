from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('E-mail',blank=True)
    def __str__(self):
        return '%s %s' %(self.first_name,self.last_name)
    
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    website = models.URLField(max_length=200)
    def __str__(self):
        return self.name
        
class Book(models.Model):
    title = models.CharField(max_length=40)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publish_date = models.DateTimeField(max_length=40)
    def __str__(self):
        return self.title
