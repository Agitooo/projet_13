from django.shortcuts import render
from .models import Profile


def index(request):
    """Sed placerat quam in pulvinar commodo"""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac"""
    profile_user = Profile.objects.get(user__username=username)
    context = {'profile': profile_user}
    return render(request, 'profiles/profile.html', context)
