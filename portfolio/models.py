from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Languages(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=3, blank=True)
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.name
