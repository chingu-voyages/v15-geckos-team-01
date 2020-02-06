from django.test import TestCase

try:
    from .models import Goal, GoalOne, GoalTwo, GoalThree, Bookmarks
except ImportError as e:
    print("An import failed:")
    print(e)

try:
    from GeckoOneHome.models import MyUser
except ImportError as e:
    print("An import failed:")
    print(e)
"""
Goal *user todo list*:
text = models.CharField(max_length=40, default="TODO list item.")
complete = models.BooleanField(default=False)
user = models.ForeignKey(MyUser, on_delete = models.CASCADE, related_name='+')

GoalOne *user, one item retrieved by first() in views*:
text = models.CharField(max_length=40, default="Your goal here>")
user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')

GoalTwo *user, one item retrieved by first() in views*
text = models.CharField(max_length=40, default="Your goal here>")
user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')

GoalThree *user, one item retrieved by first() in views*
text = models.CharField(max_length=40, default="Your goal here>")
user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')

Bookmarks *user saved urls, with nicknames*
alink = models.URLField(max_length=130, default="A website you wish to save.")
nickname = models.CharField(max_length=40, default="An easy to remember nickname for your link.")
user = models.ForeignKey(MyUser, on_delete = models.CASCADE,  related_name='+')
"""


#--------------- TEST TODO ----------------#
class GoalTest(TestCase):

    def setUp(self):
        test_user = MyUser.objects.create_user(email='foobar@aol.com', password='12345abc')
        new_user = MyUser.objects.get(email='foobar@aol.com')
        truegoal = Goal(text="make a true todo", complete=True, user=new_user)
        truegoal.save()
        falsegoal = Goal(text="make a default false todo", user=new_user)
        falsegoal.save()

    def test_newgoal(self):
        try:
            newgoal = Goal(text="make a todo", user="nonExistantUser") #expect fail
        except:
            newgoal = "try block failed"

        self.assertEqual(newgoal, "try block failed")

    def test_truegoal(self):
        new_user = MyUser.objects.get(email='foobar@aol.com')
        todo = Goal.objects.filter(user = new_user)
        first_todo = todo[0].text
        #first_todo = todo.first().text
        self.assertEqual(first_todo, "make a true todo")
        first_complete = todo[0].complete
        self.assertEqual(first_complete, True)

    def test_falsegoal(self):
        new_user = MyUser.objects.get(email='foobar@aol.com')
        todo = Goal.objects.filter(user = new_user)
        second_todo = todo[1].complete
        second_todo_text = todo[1].text
        self.assertEqual(second_todo, False)
        self.assertEqual(second_todo_text, 'make a default false todo')


