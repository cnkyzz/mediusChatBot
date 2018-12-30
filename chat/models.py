from django.db import models

class User(models.Model):
    name = models.TextField()
    sex = models.TextField()
    birth = models.DateField(auto_now_add=True)
    smoker = models.BooleanField(default=False)
    answerIndex = models.IntegerField(default=1) # current index for the questions in the order shown in example