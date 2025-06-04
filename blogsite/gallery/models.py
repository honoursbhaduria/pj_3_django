from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.charField(max_length=225)
    description = models.models.TextField()
    image = models.models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name 

    def edit(self , name , description , image ):
        self.name = name 
        self.description = description 
        self.image = image
        self.save()

    def short_description(self):

        words = self.description.split() 

        if len(words) > 50:
            return ' '.join(words[:50]) + '...'
        else:
            return self.description