from django.db import models

class Goal(models.Model):
    text = models.CharField(max_length=40, default="Your goal here>")
    complete = models.BooleanField(default=False)
    user = models.CharField(max_length=50, default="unknown user")

    def __str__(self):
        return self.text
