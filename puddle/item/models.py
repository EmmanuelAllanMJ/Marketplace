from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    # To make the plural form of the word "Category" be "Categories" instead of "Categorys"
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    # To make the name of the category show up in the admin panel
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE) # if user is deleted, delete all items created by that user
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    # To make the name of the item show up in the admin panel
    def __str__(self):
        return self.name    