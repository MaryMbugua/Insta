from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def landing(request):

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):

    return render(request,'profile.html')

@login_required(login_url='/accounts/login/')
def explore(request):

    return render(request,'search.html')
    
@login_required(login_url='/accounts/login/')
def edit(request):

    return render(request,'edit.html')