from django.db import models


# Create your models here.
class Consult(models.Model):
    name = models.CharField(max_length=16)
    position = models.CharField(max_length=16, blank=True, null=True)
    group = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=14)
    describe = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Consult'
