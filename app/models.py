from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    user=models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    sno=models.AutoField(primary_key=True)
    task=models.CharField( max_length=1000)
    deadline=models.DateTimeField( auto_now=False, auto_now_add=False)
    def __str__(self) -> str:
        return  f" {self.user}  - " +self.task 