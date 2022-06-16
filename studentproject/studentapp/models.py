from django.db import models

class Login(models.Model):
    username = models.EmailField(max_length=25)
    password = models.TextField(max_length=25)
    class Meta:
        db_table = 'login'

class Registration1(models.Model):
    name = models.TextField(max_length=25)
    contact = models.TextField(max_length=25)
    email = models.EmailField(max_length=25)
    username = models.TextField(max_length=25)
    password = models.TextField(max_length=25)
    cpassword = models.TextField(max_length=25)
    class Meta:
        db_table = 'registration'
