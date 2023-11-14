from django.db import models

# Create your models here.
class demoForm(models.Model):
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 50)
    phnumber = models.CharField(max_length = 13)
    createTime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.firstName+str(self.id)