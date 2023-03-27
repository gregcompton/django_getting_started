from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from form.forms import VehicleForm, CatForm
from form.models import Cat
import html


def example(request):
    form = VehicleForm()
    return HttpResponse(form.as_table())


# Call as dumpdata('GET' request.GET)
def dumpdata(place, data):
    retval = ""
    if len(data) >0:
        retval += f'<p>Incoming {place} data: <br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval


class DumpPostView(View):  # reusable code....
    def post(self, request):
        dump = dumpdata('POST', request.POST)
        ctx = {'title': 'request.POST', 'dump':dump}
        return render(request, 'form/dump.html', ctx)


class SimpleCreate(DumpPostView):
    def get(self, request):
        form = VehicleForm()
        ctx = {'form': form}
        return render(request, 'form/form.html', ctx)


class SimpleUpdate(DumpPostView):
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar',
            'mileage' : 42,
            'purchase_date': '2018-08-14'
        }
        form = VehicleForm(old_data)
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)


class Validate(DumpPostView):
    def get(self, request) :
        old_data = {
            'title': 'Tundra',
            'mileage' : 42,
            'purchase_date': '2018-08-14'
        }
        form = VehicleForm(initial=old_data)
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

    def post(self, request) :
        form = VehicleForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, 'form/form.html', ctx)
        # If there are no errors, we would save the data
        x = reverse('form:success')
        return redirect(x)

def success(request) :
    return HttpResponse('Thank you!')

class CatCreate(View):
    def get(self, request) :
        form = CatForm()
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

    def post(self, request) :
        form = CatForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, 'form/form.html', ctx)

        # Save the form and get a model object
        newcat = form.save()
        x = reverse('form:main') + '#' + str(newcat.id)
        return redirect(x)

class CatUpdate(View):
    def get(self, request, pk) :
        oldcat = get_object_or_404(Cat, pk=pk)
        form = CatForm(instance=oldcat)
        ctx = { 'form': form }
        return render(request, 'form/form.html', ctx)

    def post(self, request, pk) :
        oldcat = get_object_or_404(Cat, pk=pk)
        form = CatForm(request.POST, instance=oldcat)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, 'form/form.html', ctx)

        editcat = form.save()
        x = reverse('form:main')
        return redirect(x)

# References

# https://stackoverflow.com/questions/383944/what-is-a-python-equivalent-of-phps-var-dump