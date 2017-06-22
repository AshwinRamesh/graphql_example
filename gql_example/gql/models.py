from django.db import models


class User(models.Model):
    """A user"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=None, blank=True)


class Event(models.Model):
    """An event created by a single user"""

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    creator = models.ForeignKey(User)


class UserFriend(models.Model):
    """Friend pairs"""

    class Meta:
        unique_together = (
            ('user_1', 'user_2'),
        )

    user_1 = models.ForeignKey(User, related_name='user_1')
    user_2 = models.ForeignKey(User, related_name='user_2')


class UserEvent(models.Model):
    """Users attending an event"""

    class Meta:
        unique_together = (
            ('user', 'event'),
        )

    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
