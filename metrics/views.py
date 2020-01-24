from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .models import Goal, GoalOne, GoalTwo, GoalThree, Bookmarks
from .forms import GoalForm, GoalONEForm, GoalTWOForm, GoalTHREEForm, Bookmark
from django.views.decorators.http import require_POST


#------- load the page ----------#
def load_metrics(request):
    try:
        user_id = request.user

        goals_list = Goal.objects.filter(user=user_id)
        longtermgoal = GoalOne.objects.filter(user=user_id).first()
        threemonthgoal=GoalTwo.objects.filter(user=user_id).first()
        shorttermgoal = GoalThree.objects.filter(user=user_id).first()
        bookmark_list = Bookmarks.objects.filter(user=user_id)

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

        form = GoalForm()
        form4 = Bookmark()

        user_metrics = {'form': form, 'form4': form4, 'goals_list': goals_list, 'longtermgoal': longtermgoal, 'threemonthgoal': threemonthgoal, 'shorttermgoal': shorttermgoal, 'bookmark_list': bookmark_list}

        return render(request, 'metrics/metrics.html', user_metrics)

    except:
        # This is not a logged in user.
        return render(request, 'metrics/metrics.html')

# -------- Front-end  Mytrack load -----#

def load_myTrack(request):
    #    ADD USER WHEN DB UPDATED   #
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
    Goal.objects.get(pk=goal_id).delete()
    return redirect('metrics')

#------------ Add and Delete singular Goals ---------#

@require_POST
def add_GoalOne(request):
    form1 = GoalONEForm(request.POST)
    form2 = GoalTWOForm(request.POST)
    form3 = GoalTHREEForm(request.POST)
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
            return redirect('myTrack')
        else:
            new_goal = GoalOne(text=new_text, user=user_id)
            new_goal.save()
            return redirect('myTrack')
    else:
        try:


            longtermgoal = GoalOne.objects.filter(user=user_id).first()
            threemonthgoal=GoalTwo.objects.filter(user=user_id).first()
            shorttermgoal = GoalThree.objects.filter(user=user_id).first()
            if longtermgoal == None:
                longtermgoal = "No long term goal is set."

            if threemonthgoal == None:
                threemonthgoal = "No three month goal is set."

            if shorttermgoal == None:
                shorttermgoal = "No short term goal is set."


            user_metrics = {'form1': form1, 'form2': form2, 'form3': form3, 'longtermgoal': longtermgoal, 'threemonthgoal': threemonthgoal, 'shorttermgoal': shorttermgoal}


            return render(request, 'metrics/mytrack.html', user_metrics)
        except:

            return render(request, 'metrics/mytrack.html')


#--------------  Add/Edit GoalTwo ----------------#

@require_POST
def add_GoalTwo(request):
    form1 = GoalONEForm(request.POST)
    form2 = GoalTWOForm(request.POST)
    form3 = GoalTHREEForm(request.POST)
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
            return redirect('myTrack')
        else:
            new_goal = GoalTwo(text=new_text, user=user_id)
            new_goal.save()
            return redirect('myTrack')
    else:
        try:
            longtermgoal = GoalOne.objects.filter(user=user_id).first()
            threemonthgoal=GoalTwo.objects.filter(user=user_id).first()
            shorttermgoal = GoalThree.objects.filter(user=user_id).first()
            if longtermgoal == None:
                longtermgoal = "No long term goal is set."

            if threemonthgoal == None:
                threemonthgoal = "No three month goal is set."

            if shorttermgoal == None:
                shorttermgoal = "No short term goal is set."


            user_metrics = {'form1': form1, 'form2': form2, 'form3': form3, 'longtermgoal': longtermgoal, 'threemonthgoal': threemonthgoal, 'shorttermgoal': shorttermgoal}


            return render(request, 'metrics/mytrack.html', user_metrics)

        except:

            return render(request, 'metrics/mytrack.html')


#---------  Add/edit Goal 3 short term goal -----#
@require_POST
def add_GoalThree(request):
    form1 = GoalONEForm(request.POST)
    form2 = GoalTWOForm(request.POST)
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
            return redirect('myTrack')
        else:
            new_goal = GoalThree(text=new_text, user=user_id)
            new_goal.save()
            return redirect('myTrack')
    else:
        try:
            longtermgoal = GoalOne.objects.filter(user=user_id).first()
            threemonthgoal=GoalTwo.objects.filter(user=user_id).first()
            shorttermgoal = GoalThree.objects.filter(user=user_id).first()
            if longtermgoal == None:
                longtermgoal = "No long term goal is set."

            if threemonthgoal == None:
                threemonthgoal = "No three month goal is set."

            if shorttermgoal == None:
                shorttermgoal = "No short term goal is set."


            user_metrics = {'form1': form1, 'form2': form2, 'form3': form3, 'longtermgoal': longtermgoal, 'threemonthgoal': threemonthgoal, 'shorttermgoal': shorttermgoal}


            return render(request, 'metrics/mytrack.html', user_metrics)
        except:

            return render(request, 'metrics/mytrack.html')

#----  Bookmarks --------------#


@require_POST
def add_Bookmark(request):


    form4 = Bookmark(request.POST)

    if form4.is_valid():
        user_id = request.user
        new_URL = request.POST['alink']
        new_nickname = request.POST['nickname']
        # IMPORTANT:  request.POST['text'] will not pass in properly, base10 error
        # must be translated into a variable, and then passed to the model Goal.
        #print("\n\n text = \n\n", text)
        new_bookmark = Bookmarks(alink=new_URL, nickname=new_nickname, user=user_id)

        new_bookmark.save()

    return redirect('metrics')


def delete_Bookmark(request, url_id):
    Bookmarks.objects.get(pk=url_id).delete()
    return redirect('metrics')



