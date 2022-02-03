from django.db import models


class Counter(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.count