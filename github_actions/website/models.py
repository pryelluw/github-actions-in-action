from django.db import models


class Page(models.Model):
    name = models.CharField(unique=True)
    slug - models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
