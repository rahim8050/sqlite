from django.db import models

# Create your models here.
class customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=50)

# python  manage.py makemigrations
# python manage.py migrate
