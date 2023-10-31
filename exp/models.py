from django.db import models
import django.utils
from datetime import datetime as dt
from django.contrib.auth.models import User


def timestamp():
    return int(dt.timestamp(django.utils.timezone.now()))


def name_image():
    return str(timestamp())


class Expense(models.Model):
    sno = models.AutoField(db_column='sno', primary_key=True)
    timestamp = models.BigIntegerField(db_column='timestamp', default=timestamp)
    exp_type = models.CharField(db_column='exp_type', max_length=25)
    sub_type = models.CharField(db_column='sub_type', max_length=25)
    amount = models.IntegerField(db_column='amount')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User object must be assigned to 'user', django automatically access id for db


class Schedule(models.Model):
    sno = models.AutoField(db_column='sno', primary_key=True)
    timestamp = models.BigIntegerField(db_column='timestamp', default=timestamp)
    exp_type = models.CharField(db_column='exp_type', max_length=25)
    sub_type = models.CharField(db_column='sub_type', max_length=25)
    amount = models.IntegerField(db_column='amount')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User object must be assigned to 'user', django automatically access id for db


class Image(models.Model):
    name = models.CharField(default=name_image, max_length=20)
    img = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User object must be assigned to 'user', django automatically access id for db
