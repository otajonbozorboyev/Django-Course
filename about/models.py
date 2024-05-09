from django.db import models

class About(models.Model):
    full_name = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='about/')
    description = models.TextField()
    twitter = models.CharField(max_length=202)
    facebook = models.CharField(max_length=202)
    instagram = models.CharField(max_length=202)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.full_name
    

class Section(models.Model):
    title = models.CharField(max_length=202)
    numbers = models.IntegerField()

    def __str__(self):
        return self.title