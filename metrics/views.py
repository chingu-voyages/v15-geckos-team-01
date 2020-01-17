from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate


def load_metrics(request):
    return render(request, 'metrics/metrics.html')
