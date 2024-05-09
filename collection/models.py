from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='collection/')

    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title