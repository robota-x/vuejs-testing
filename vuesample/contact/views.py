from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from . import forms
from . import models


def index(request):
    form = forms.EnquiryForm(request.POST or None)

    # deal with vue posting the data
    if request.POST:
        if form.is_valid():
            form.save()
            return JsonResponse(status=201, data={})
        else:
            return JsonResponse(status=400, data=form.errors)

    return render(request, 'contact/index.html', {'form': form})

def office(request, id=None):
    if id:
        offices = convert_obj(get_object_or_404(models.Office, pk=id))
    else:
        offices = [convert_obj(obj) for obj in models.Office.objects.all()]

    return JsonResponse(offices, safe=False)

def convert_obj(obj):
    return {
        'latitude': obj.latitude,
        'longitude': obj.longitude,
        'name': obj.name,
        'description': obj.description
    }