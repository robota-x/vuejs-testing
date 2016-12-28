from django.http import HttpResponse
from django.shortcuts import render

from . import forms


def index(request):
    form = forms.EnquiryForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        else:
            return None

    return render(request, 'contact/index.html', {'form': form})

