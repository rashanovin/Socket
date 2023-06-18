from django.db import models


class CustomChat(models.Model):
    question = models.CharField(max_length=500, unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.question
