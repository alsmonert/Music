from django.db import models
import string
import random


def generate_code():
    lenght = 6
    while True:
        code = ''.join(random.choice(string.ascii_uppercase, k=lenght))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


class Room(models.Model):
    code = models.CharField(max_length=8, default=generate_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_pause = models.BooleanField(null=False, default=False)
    votes_skip = models.IntegerField(null=False, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
