from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=None, blank=True)


class Event(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    creator = models.ForeignKey(User)


class UserFriend(models.Model):
    user_1 = models.ForeignKey(User, related_name='user_1')
    user_2 = models.ForeignKey(User, related_name='user_2')
