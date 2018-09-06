from django.db import models


# Create your models here.

class Consult(models.Model):
    name = models.CharField(max_length=16)
    position = models.CharField(max_length=16)
    group = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    describe = models.TextField()
    file = models.FileField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Consult'
