from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=202)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title