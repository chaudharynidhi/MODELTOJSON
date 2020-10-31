from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

class ActivityPeriod(models.Model):
    start_time = models.CharField(max_length=250)
    end_time = models.CharField(max_length=250)
    activity_id = models.ForeignKey(Users, on_delete=models.CASCADE)    