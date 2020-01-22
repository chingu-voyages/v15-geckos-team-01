from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .models import Goal, GoalOne, GoalTwo, GoalThree
from .forms import GoalForm, GoalONEForm, GoalTWOForm, GoalTHREEForm
from django.views.decorators.http import require_POST


#------- load the page ----------#
def load_metrics(request):
    user_id = request.user

    goals_list = Goal.objects.filter(user_id=user_id)
    if goals_list:
        form = GoalForm()
        user_metrics = {'form': form, 'goals_list': goals_list}
        return render(request, 'metrics/metrics.html', user_metrics)

    else:
        form = GoalForm()
        goals_list = ["no task items currently set.", "Use ADD button to add a to-do."]
        user_metrics = {'form': form, 'goals_list': goals_list}

        return render(request, 'metrics/metrics.html', user_metrics)

# -------- Front-end  Mytrack load -----#

def load_myTrack(request):
    #    ADD USER WHEN DB UPDATED   #
    return render(request, 'metrics/mytrack.html')

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
        new_goal = Goal(text=new_text, user_id=user_id)

        new_goal.save()
    return redirect('metrics')


def deleteGoal(request, goal_id):
    Goal.objects.get(pk=goal_id).delete()
    return redirect('metrics')

#------------ Add and Delete singular Goals ---------#

@require_POST
def add_GoalOne(request):
    form = GoalONEForm(request.POST)

    if form.is_valid():
        user_id = request.user
        new_text = request.POST['text']
        # IMPORTANT:  request.POST['text'] will not pass in properly, base10 error
        # must be translated into a variable, and then passed to the model Goal.
        #print("\n\n text = \n\n", text)
        new_goal = GoalOne(text=new_text, user_id=user_id)

        new_goal.save()
    return redirect('metrics')






