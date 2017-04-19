from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import *
from django.contrib.auth import authenticate, login, logout
from core.forms import SignUpForm, UploadForm
from core.models import Dataset
from django.contrib.auth.models import User
import pandas as pd
from StringIO import StringIO


def index(request):
    user = request.user
    return render_to_response('core/home.html', {"user":user})

def signup(request):
    logout(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return render_to_response('core/home.html', {"user":user})
    else:
        form = SignUpForm()
    return render(request,'core/signup.html',{'form':form})

def start(request):
    user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.creator = User.objects.get(username=user)
            dataset.sep = "\t"
            dataset.save()
    form = UploadForm()
    datasets = Dataset.objects.filter(creator=user)
    dataset_tables = []
    for dataset in datasets:
        dataset_tables.append(pd.read_csv(StringIO(dataset.data),sep=dataset.sep).to_html())
    return render(request,'core/start.html', {"user":user,"datasets":datasets,"form":form,"dataset_tables":dataset_tables})

def gallery(request):
    user = request.user
    return render_to_response('core/gallery.html', {"user":user})
        
