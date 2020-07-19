from django.db import models

# Create your models here.
class Emails(models.Model):
    email_from = models.CharField(max_length=200)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email_from
