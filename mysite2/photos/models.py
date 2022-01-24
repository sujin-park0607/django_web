from django.db import models


class Photo(models.Model):
    image = models.ImageField(null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.description
# Create your models here.
