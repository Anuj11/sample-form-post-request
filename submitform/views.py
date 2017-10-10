# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.conf import settings
from submitform.models import submit
from submitform.forms import SubmitForm
# Create your views here.

def home(request):
    information = submit.objects.all().order_by('-id')

    return render(request, 'core/home.html', { 'information': information })

def model_form_upload(request):
    form_class = SubmitForm
    form = form_class(request.POST or None)
    if request.method == 'POST':

    #    form = form_class(request.POST)
        if form.is_valid():

            form.save()
            return redirect('home')
    else:
        form = SubmitForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
