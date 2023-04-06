from django.shortcuts import render
from django.views import View
from django.conf import settings

from social_django.models import AbstractUserSocialAuth, UserSocialAuth

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }

        if request.user.is_authenticated:
            print(request.user.username)
            for e in UserSocialAuth.objects.filter(user=request.user):
                print(e.user, e.provider)


        return render(request, 'home/main.html', context)