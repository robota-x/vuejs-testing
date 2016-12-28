from django.http import JsonResponse
from django.shortcuts import render

from . import forms


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

