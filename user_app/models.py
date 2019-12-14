from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=120)
    contact = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    reputation = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
