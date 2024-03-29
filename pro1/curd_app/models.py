from django.db import models


class School(models.Model):
    gen = [('BOY', 'boy'), ('GIRL', 'girl'), ('OTHER', 'other')]
    child_name = models.CharField(max_length=20)
    parent_name = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=gen)
    home_address = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)




