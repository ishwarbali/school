from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
