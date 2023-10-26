from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo
def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
def profile(request, username):
    profile_user = Profile.objects.get(user__username=username)
    context = {'profile': profile_user}
    return render(request, 'profiles/profile.html', context)
