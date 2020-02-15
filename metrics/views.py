from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .models import Goal, GoalOne, GoalTwo, GoalThree, Bookmarks
from .forms import GoalForm, GoalONEForm, GoalTWOForm, GoalTHREEForm, Bookmark
from django.views.decorators.http import require_POST


#------- load the page ----------#
def load_metrics(request):
    """
    INFO:
    form 1-3 are for setting a the first item in the list of one of the three
    goals, a long term *GoalONEForm, three month *GoalTWOForm, and current 1-month goal *GoalTHREEForm.

    --- user_metrics items---
    goals_list is a list of todo text strings the user sets in the database via the Todo list UI in html.
    The django uses a for loop to display all the items in the list, or defaults provided in this function.

    longtermgoal, threemonthgoal, and shorttermgoal are the first item in the object related one of these:
    longtermgoal: GoalOne object
    threemonthgoal: GoalTwo object
    shorttermgoal: GoalThree object
    All of these objects are defined in the models.py of this directory.
    There is only one item saved per user per object, and since I haven't found a better way to save a singular
    text line, I used the *.first() django built in to retrieve either the first item, or None (if the list object is empty).

    bookmark_list uses the object-model Bookmarks defined in the models.py of this directory.
    It stores a valid url string as the alink, and a nickname of the users choosing to describe that link.

    If any of the user_metrics models are empty, user has deleted them all or they have not created any, this
    will send default text in the place of these items so that error are not thrown by empty-NoneType data.
    """
    form = GoalForm(request.POST)
    form1 = GoalONEForm(request.POST)
    form2 = GoalTWOForm(request.POST)
    form3 = GoalTHREEForm(request.POST)
    form4 = Bookmark(request.POST)
    # If user is not authenticated, logged in, send them to a demo page
    # data base items are stored by unique keys, related to thier user email upon registration
    if request.user.is_authenticated:
        try:
            user_id = request.user

            goals_list = Goal.objects.filter(user=user_id)
            longtermgoal = GoalOne.objects.filter(user=user_id).first()
            threemonthgoal=GoalTwo.objects.filter(user=user_id).first()
            shorttermgoal = GoalThree.objects.filter(user=user_id).first()
            bookmark_list = Bookmarks.objects.filter(user=user_id)
            # If they have not set an item, send a placeholder for the missing item instead
            # This is required because the html calls these items in the displayed html
            # not providing a these placeholders can lead to errors when Django looks for an item that doesn't exist.
            if not goals_list:
                goals_list = ["no task items currently set.", "Use ADD button to add a to-do."]
            if longtermgoal == None:
                longtermgoal = "You have not set a long term goal yet."
            if threemonthgoal == None:
                threemonthgoal = "You have not set a three month goal yet."
            if shorttermgoal == None:
                shorttermgoal = "You have not set your short term goal yet."
            if not bookmark_list:
                bookmark_list = [" save some bookmarks here ", "keep them in one place for easier retrieval!", "nickname your links to make them easier to identify"]


            # send all the items that django loads into the html in this dictionary *user_metrics
            user_metrics = {'form': form, 'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'goals_list': goals_list, 'longtermgoal': longtermgoal, 'threemonthgoal': threemonthgoal, 'shorttermgoal': shorttermgoal, 'bookmark_list': bookmark_list}

            return render(request, 'metrics/MyTrack.html', user_metrics)

        except:
            # This is not a logged in user.
            # send them to a demo page which does not have access to any database items
            return render(request, 'metrics/MyTrack_Demo.html')
    else:
        #upon any failure inside the try block, send user to a Demo page that does not have access to the database
        return render(request, 'metrics/MyTrack_Demo.html')

# -------- Front-end  Mytrack load  **Not In Use** -----#

def load_myTrack(request):
    #   This was a sample view for testing and loading purposed goals UI  #
    form1 = GoalONEForm(request.POST)
    form2 = GoalTWOForm(request.POST)
    form3 = GoalTHREEForm(request.POST)
    try:
        user_id = request.user

        longtermgoal = GoalOne.objects.filter(user=user_id).first()
        threemonthgoal=GoalTwo.objects.filter(user=user_id).first()
        shorttermgoal = GoalThree.objects.filter(user=user_id).first()
        if longtermgoal == None:
            longtermgoal = "No long term goal is set."

        if threemonthgoal == None:
            threemonthgoal = "No three month goal is set."

        if shorttermgoal == None:
            shorttermgoal = "No short term goal is set."


        return render(request, 'metrics/mytrack.html', {'form1': form1,'form2': form2, 'form3': form3, 'longtermgoal': longtermgoal, 'threemonthgoal': threemonthgoal, 'shorttermgoal': shorttermgoal})
    except:
        return render(request, 'metrics/mytrack.html', {'form1': form1, 'form2': form2, 'form3': form3})


#---------- Add and delete Goals(model) (now the TODO) ---------#
@require_POST
def addGoal(request):
    """
    Used to retrieve a new model object that will store a to-do item in a list for use as the
    *goals_list in html redering.  The user's todo list is stored via their registered email address.
    """

    form = GoalForm(request.POST)

    if form.is_valid():
        user_id = request.user
        new_text = request.POST['text']
        # IMPORTANT:  request.POST['text'] will not pass in properly, base10 error
        # must be translated into a variable, and then passed to the model Goal.
        #print("\n\n text = \n\n", text)
        new_goal = Goal(text=new_text, user=user_id)

        new_goal.save()

    return redirect('metrics')


def deleteGoal(request, goal_id):
    # if user has clicked the icon/link to delete an item, it will be immediatedely removed from
    # the database and not recoverable.  They can add valid string items to the database at any time.
    Goal.objects.get(pk=goal_id).delete()
    return redirect('metrics')

def editToDo(request, todo_id):
    pass

#------------ Add and Delete singular Goals ---------#
"""
INFO on singular goals:
add_GoalOne(request)
add_GoalTwo(request)
add_GoalThree(request)

Upon unsuccessful form validation, the metrics page will be reloaded with a redirect database is unchanged.
Redirect to 'metrics' will send a message through django to run the views.py function *load_metrics(request).
This method has checks for user auth and all user data variables for html defined in *user_metrics
"""

@require_POST
def add_GoalOne(request):
    # Upon unsuccessful form validation, the metrics page will be reloaded with a redirect
    # database is unchanged.
    # redirect to 'metrics' will send a message through django to run the views.py
    # function *load_metrics(request).  This method has checks and these forms defined.
    # as well as all *user_metrics
    form1 = GoalONEForm(request.POST)


    user_id = request.user


    if form1.is_valid():
        user_id = request.user
        new_text = request.POST['text']

        # IMPORTANT:  request.POST['text'] will not pass in properly, base10 error
        # must be translated into a variable, and then passed to the model GoalOne.
        old_goal = GoalOne.objects.filter(user=user_id).first()

        if old_goal:

            old_goal.text = new_text

            old_goal.save()
            return redirect('metrics')
        else:
            new_goal = GoalOne(text=new_text, user=user_id)
            new_goal.save()
            return redirect('metrics')
    else:


            return render(request, 'metrics')


#--------------  Add/Edit GoalTwo ----------------#

@require_POST
def add_GoalTwo(request):

    form2 = GoalTWOForm(request.POST)

    user_id = request.user

    if form2.is_valid():
        user_id = request.user
        new_text = request.POST['text']

        # IMPORTANT:  request.POST['text'] will not pass in properly, base10 error
        # must be translated into a variable, and then passed to the model GoalOne.
        old_goal = GoalTwo.objects.filter(user=user_id).first()

        if old_goal:

            old_goal.text = new_text

            old_goal.save()
            return redirect('metrics')
        else:
            new_goal = GoalTwo(text=new_text, user=user_id)
            new_goal.save()
            return redirect('metrics')
    else:
        return render(request, 'metrics')


#---------  Add/edit Goal 3 short term goal -----#
@require_POST
def add_GoalThree(request):

    form3 = GoalTHREEForm(request.POST)

    user_id = request.user

    if form3.is_valid():
        user_id = request.user
        new_text = request.POST['text']

        # IMPORTANT:  request.POST['text'] will not pass in properly, base10 error
        # must be translated into a variable, and then passed to the model GoalOne.
        old_goal = GoalThree.objects.filter(user=user_id).first()
        if old_goal:

            old_goal.text = new_text

            old_goal.save()
            return redirect('metrics')
        else:
            new_goal = GoalThree(text=new_text, user=user_id)
            new_goal.save()
            return redirect('metrics')
    else:
        return render(request, 'metrics')

#----  Bookmarks --------------#


@require_POST
def add_Bookmark(request):


    form4 = Bookmark(request.POST)

    if form4.is_valid():
        user_id = request.user
        new_URL = request.POST['alink']
        new_nickname = request.POST['nickname']
        # IMPORTANT:  request.POST['text'] will not pass in properly, base10 error
        # must be translated into a variable, and then passed to the model.
        #print("\n\n text = \n\n", text)
        new_bookmark = Bookmarks(alink=new_URL, nickname=new_nickname, user=user_id)

        new_bookmark.save()

    return redirect('metrics')


def delete_Bookmark(request, url_id):
    Bookmarks.objects.get(pk=url_id).delete()
    return redirect('metrics')



def edit_bookmark(request, url_id):
    item = Bookmarks.objects.get(pk=url_id)
    form = Bookmark(request.POST)
    old_url = item.alink
    old_nickname = item.nickname


    return render(request, 'metrics/edit_bookmarks.html', {'form': form, 'old_url': old_url, 'old_nickname': old_nickname, 'item': item})


@require_POST
def change_bookmark(request, url_id):
    item = Bookmarks.objects.get(pk=url_id)
    form = Bookmark(request.POST)
    old_url = item.alink
    old_nickname = item.nickname
    if form.is_valid():
        item.alink = request.POST['alink']
        item.nickname = request.POST['nickname']
        item.save()
        return redirect('metrics')
    else:
        return render(request, 'metrics/edit_bookmarks.html', {'form': form, 'old_url': old_url, 'old_nickname': old_nickname})










