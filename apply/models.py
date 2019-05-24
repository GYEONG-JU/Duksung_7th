from django.db import models

# Create your models here.

class apply(models.Model):
    name = models.CharField(max_length=30)
    major = models.CharField(max_length=30,null=True)
    student_id = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    body = models.TextField(null=True)
    file = models.FileField(null=True)
    isFinal = models.CharField(max_length=10,null=True)

    def __str__ (self):
        return self.title
