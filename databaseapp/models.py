from unittest.util import _MAX_LENGTH
from django.db import models

# Create model called User
# It's have to have these fields
# first_name, last_name, email, phone_number

class User_person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=40)