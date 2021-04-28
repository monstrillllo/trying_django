from django.shortcuts import render
from .models import Titles


# Create your views here.

def index(request):
    return render(request, 'anime_lists/index.html')


def titles(request):
    """ getting titles from db """
    all_titles = Titles.objects.order_by('date_added')
    context = {'titles': all_titles}
    return render(request, 'anime_lists/titles.html', context)


def title(request, title_id):
    """ getting info about particular title"""
    title1 = Titles.objects.get(id=title_id)
    entries = title1.entry_set.order_by('-date_added')
    context = {'title': title, 'entries': entries}
    return render(request, 'anime_lists/title.html', context)

