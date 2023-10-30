from django.shortcuts import render
from .models import Letting


def index(request):
    """Aenean leo magna, vestibulum et tincidunt fermentum,
    consectetur quis velit. Sed non"""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Cras ultricies dignissim purus, vitae hendrerit ex varius non.
    In accumsan porta nisl id eleifend."""
    letting_obj = Letting.objects.get(id=letting_id)
    context = {
        'title': letting_obj.title,
        'address': letting_obj.address,
    }
    return render(request, 'lettings/letting.html', context)
