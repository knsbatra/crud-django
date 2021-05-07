from django.db import models
import datetime


class Employee(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=1000)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    group = models.CharField(max_length=20)
    bike = models.BooleanField(default=False)
    car = models.BooleanField(default=False)
    boat = models.BooleanField(default=False)
    dob = models.DateField(default=datetime.date.today)
    years = models.BooleanField()
    pic = models.ImageField(null=True, blank=True, upload_to="images/")
    amount = models.FloatField()

    class Meta:
        db_table = 'Employee'
