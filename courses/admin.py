from django.contrib import admin

from courses.models import Course, Membership, Person

admin.site.register(Course)
admin.site.register(Membership)
admin.site.register(Person)
