from django.db import models

# Create your models here.

# class UserProfile_table(models.Model):
#     Name
#     email
#     user_id
#     photo
#     phone_number


class User_table(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)