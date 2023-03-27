'''
documentation on auth and mixins
https://docs.djangoproject.com/en/4.1/topics/auth/default/
https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.mixins.AccessMixin
'''

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.utils.http import urlencode

from django.contrib.auth.models import Permission
from django.http import HttpResponse


class OpenView(View):
    def get(self, request):
        return render(request, 'authz/main.html')


class ApereoView(View):
    def get(self, request):
        return render(request, 'authz/main.html')


class ManualProtect(View):
    def get(self, request):
        if not request.user.is_authenticated:
            loginurl = reverse('login') + '?' + urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'authz/main.html')


class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'authz/main.html')


class PermissionView(PermissionRequiredMixin, View):
    permission_required = 'autos.add_auto'


class UserTestView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.email.endswith('@gregcompton.com')

    def get(self, req):
        return render(req, 'authz/main.html')

    def get(self, request):
        return render(request, 'authz/main.html')


class DumpPython(View):
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
            permissions = self.get_user_permissions(req.user)
            resp += f'Last login: {req.user.last_login}\n\n'
            resp += "Permissons\n"
            for p in permissions:
                resp += f'app: {p.content_type.app_label} | model: {p.content_type.model} | name: {p.name}\n'
                resp += f'\t{p}\n----------------------------------------------------\n'
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/authz">Go back</a>"""

        print(f'is staff: {req.user.is_staff}')
        return HttpResponse(resp)

    def get_user_permissions(self, user):
        if user.is_superuser:
            return Permission.objects.all()
        return user.user_permissions.all() | Permission.objects.filter(group__user=user)
