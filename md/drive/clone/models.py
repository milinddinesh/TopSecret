from django.db import models

# Create your models here.
# class FilesUpload(models.Model):
    # file = models.FileField()

class Files_Upload(models.Model):
    filename = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='media/users/')

    def __str__(self) :
        return self.title