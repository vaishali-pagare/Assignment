from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    phone = models.IntegerField()
    password = models.CharField(max_length=15)
    user = models.CharField(max_length=10)
    class Meta:
        db_table = "User"

class UserImage(models.Model):
    u1 = models.ForeignKey(to="User", on_delete=models.CASCADE)
    image = models.ImageField(default='abc.jpg', upload_to='images')


    class Meta:
        db_table = "UserImage"