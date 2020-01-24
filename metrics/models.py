from django.db import models
from GeckoOneHome.models import MyUser


class Goal(models.Model):
    text = models.CharField(max_length=40, default="Your goal here>")
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE, related_name='+')


    def __str__(self):
        return self.text

class ToDo(models.Model):
    text = models.CharField(max_length=50, default="Your todo list item here>")
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')

    def __str__(self):
        return self.text


class Bookmarks(models.Model):
    alink = models.URLField(max_length=130, default="A website you wish to save.")
    nickname = models.CharField(max_length=40, default="An easy to remember nickname for your link.")
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')

    def __str__(self):
        return self.alink


class GoalOne(models.Model):
    text = models.CharField(max_length=40, default="Your goal here>")
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')

    def __str__(self):
        return self.text

class GoalTwo(models.Model):
    text = models.CharField(max_length=40, default="Your goal here>")
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')

    def __str__(self):
        return self.text

class GoalThree(models.Model):
    text = models.CharField(max_length=40, default="Your goal here>")
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')

    def __str__(self):
        return self.text

