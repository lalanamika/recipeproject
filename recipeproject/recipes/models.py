from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    add_date = models.DateTimeField()
    # user is logged in at this point, connects User db object to this Post object
    author = models.ForeignKey(User, on_delete=models.CASCADE)
