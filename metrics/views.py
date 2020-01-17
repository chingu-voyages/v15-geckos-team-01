from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .models import Goal


def load_metrics(request):
    goals_list = Goal.objects.order_by('id')
    user_metrics = {'goals_list' : goals_list}
    return render(request, 'metrics/metrics.html', user_metrics)
