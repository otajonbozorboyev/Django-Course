from django.db import models


class ContactMe(models.Model):
    address = models.CharField(max_length=202)
    phone = models.CharField(max_length=202)
    email = models.EmailField()
    website = models.CharField(max_length=202)

    def __str__(self) -> str:
        return self.phone



class Contact(models.Model):
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    message = models.TextField()

    is_published = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.full_name