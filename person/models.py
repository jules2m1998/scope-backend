from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(blank=True)
    sex = models.CharField(max_length=1, blank=True)
    birth_day = models.DateField(blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True)


class Image(models.Model):
    fullPictureLocation = models.ImageField(upload_to="picture/person", max_length=100, default="")
    headPictureLocation = models.CharField(max_length=500, default="")
    encode = models.IntegerField(default=0)
    flag = models.CharField(max_length=50, default=0)
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
