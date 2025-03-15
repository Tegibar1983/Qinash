from django.db import models
from django.contrib.auth.models import User

# data base model for item app categories

class Category(models.Model):
    #Category database model
    name=models.CharField(max_length=255)


    class Meta:
        ordering=('name',)
        #change categors to Categories
        verbose_name_plural = "Categories"

    def __str__(self):
        # change arbitrary name definition to acctual object naming"""
        return self.name
    
class Item(models.Model):
    #Items DB model
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    price=models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # change arbitrary name definition to acctual object naming"""
        return self.name