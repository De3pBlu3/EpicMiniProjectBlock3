# myapp/models.py
from django.db import models

class user_model(models.Model):
    # users(username, type, password_hash, address, registered)
    username = models.CharField(max_length=255)
    type = models.IntegerField()
    password_hash = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    registered = models.BooleanField()

    class Meta:
        db_table = 'users'
