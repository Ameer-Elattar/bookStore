from django.db import models
from django.shortcuts import  reverse,get_object_or_404
from category.models import Category



# Create your models here.
# create model Book(title , no_of_page, author, price, image, created_at, updated_at)

class Book(models.Model):
    ## define columns  ---> datatypes
    title = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=100)
    no_of_page = models.IntegerField( blank=True)
    price = models.IntegerField( blank=True)
    image = models.ImageField(upload_to='books/images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.title}'

    @property
    def showURL(self):
        url = reverse('bookShow', args=[self.id])
        return url

    @property
    def deleteURL(self):
        url = reverse('bookDelete', args=[self.id])
        return url

    @property
    def imageURL(self):
        return f"/media/{self.image}"
    
    @classmethod
    def get_book_by_id(cls,id):
        return get_object_or_404(cls,pk=id)