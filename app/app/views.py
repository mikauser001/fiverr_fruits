from django.shortcuts import render, redirect

from .forms import *
from .models import Smoothie


def index(request):
    return render(request, "landing.html", {})


def form(request):

    if request.POST:
        form = None

    return render(request, "form.html", {"form": form})


def review(request, ids):
    smoothies = Smoothie.objects.filter(id__in=ids)
    return render(request, "review.html", {"smoothies": smoothies})