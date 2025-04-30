from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'event')
