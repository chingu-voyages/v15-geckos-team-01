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


#-----------  Test GoalOne aka longtermgoal ----------------#

class LongtermTest(TestCase):
    def setUp(self):
        MyUser.objects.create_user(email='foobar2@aol.com', password='12345abc')
        new_user = MyUser.objects.get(email='foobar2@aol.com')
        # views.py uses django's built in 'first()' to grab the first item in the list.
        # list is linked by foreign key to the user object.
        # we only want the to create, edit, and submit to the index[0] item of this database list.

        new_longtermgoal = GoalOne(text='create a first longtermgoal', user= new_user)
        new_longtermgoal.save()

    def test_replacegoal(self):
        new_user = MyUser.objects.get(email='foobar2@aol.com')
        first_set_longtermgoal = GoalOne.objects.filter(user= new_user).first()
        goal_text = first_set_longtermgoal.text
        self.assertEqual(goal_text, 'create a first longtermgoal')
        first_set_longtermgoal.text = 'setting a new first longtermgoal.'
        first_set_longtermgoal.save()
        new_text = GoalOne.objects.filter(user= new_user).first()
        new_goal_text = new_text.text
        self.assertEqual(new_goal_text, 'setting a new first longtermgoal.')

#----------  Test GoalTwo aka threemonthgoal --------------#
class threemonthTest(TestCase):
    def setUp(self):
        MyUser.objects.create_user(email='foobar3@aol.com', password='12345abc')
        new_user = MyUser.objects.get(email='foobar3@aol.com')
        # views.py uses django's built in 'first()' to grab the first item in the list.
        # list is linked by foreign key to the user object.
        # we only want the to create, edit, and submit to the index[0] item of this database list.

        new_threemonth = GoalTwo(text='create a first three month goal', user= new_user)
        new_threemonth.save()

    def test_replacegoal(self):
        new_user = MyUser.objects.get(email='foobar3@aol.com')
        first_set_threemonth = GoalTwo.objects.filter(user= new_user).first()
        goal_text = first_set_threemonth.text
        self.assertEqual(goal_text, 'create a first three month goal')
        first_set_threemonth.text = 'setting a new first three month goal.'
        first_set_threemonth.save()
        new_text = GoalTwo.objects.filter(user= new_user).first()
        new_goal_text = new_text.text
        self.assertEqual(new_goal_text, 'setting a new first three month goal.')

#------------- Test GoalThree aka shorttermgoal --------------------#

class shorttermTest(TestCase):
    def setUp(self):
        MyUser.objects.create_user(email='foobar4@aol.com', password='12345abc')
        new_user = MyUser.objects.get(email='foobar4@aol.com')
        # views.py uses django's built in 'first()' to grab the first item in the list.
        # list is linked by foreign key to the user object.
        # we only want the to create, edit, and submit to the index[0] item of this database list.

        new_shortterm = GoalThree(text='create a first short term goal', user= new_user)
        new_shortterm.save()

    def test_replacegoal(self):
        new_user = MyUser.objects.get(email='foobar4@aol.com')
        first_set_shortterm = GoalThree.objects.filter(user= new_user).first()
        goal_text = first_set_shortterm.text
        self.assertEqual(goal_text, 'create a first short term goal')
        first_set_shortterm.text = 'setting a new short term goal.'
        first_set_shortterm.save()
        new_text = GoalThree.objects.filter(user= new_user).first()
        new_goal_text = new_text.text
        self.assertEqual(new_goal_text, 'setting a new short term goal.')

#-------------   Test Bookmarks -----------------#

class BookmarkTest(TestCase):
    def setUp(self):
        MyUser.objects.create_user(email='foobar5@aol.com', password='12345abc')
        new_user = MyUser.objects.get(email='foobar5@aol.com')

        # bookmarks save a valid URL, and a nickname from the user.
        # URL's are put in the href of a link, and nickname in the innerHTML for users to click

        new_bookmark_link = 'https://en.wikipedia.org/wiki/Google_bombing'
        new_nickname = 'What is a google bomb?'

        bookmark1 = Bookmarks(alink=new_bookmark_link, nickname=new_nickname, user=new_user)
        bookmark1.save()

    def test_get_bookmark(self):
        user_5 = MyUser.objects.get(email='foobar5@aol.com')
        bookmark_list = Bookmarks.objects.filter(user=user_5)
        first_in = bookmark_list[0]
        self.assertEqual(first_in.alink, 'https://en.wikipedia.org/wiki/Google_bombing')
        self.assertEqual(first_in.nickname, 'What is a google bomb?')

    def test_edit_bookmark(self):
        user_5 = MyUser.objects.get(email='foobar5@aol.com')
        bookmark_list = Bookmarks.objects.filter(user = user_5)
        first_in = bookmark_list[0]
        new_alink = 'https://en.wikipedia.org/wiki/Search_engine_optimization'
        new_nickname = 'What is SEO?'

        first_in.alink = new_alink
        first_in.nickname = new_nickname
        first_in.save()

        changed_bookmark = Bookmarks.objects.filter(user = user_5).first()
        self.assertEqual(changed_bookmark.alink, 'https://en.wikipedia.org/wiki/Search_engine_optimization')
        self.assertEqual(changed_bookmark.nickname, 'What is SEO?')









