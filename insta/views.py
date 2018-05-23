from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewPhotoForm,NewProfileForm
from .models import Profile,Image
# Create your views here.
def landing(request):
    images = Image.objects.all()
    

    return render(request,'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile1=Profile.objects.get(id=request.user.id)
    form = NewPhotoForm(request.POST,request.FILES)
    if request.method == 'POST': 
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = profile1
            image.save()
    else:
        form = NewPhotoForm()
    return render(request,'profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def explore(request):

    return render(request,'search.html')

@login_required(login_url='/accounts/login/')
def edit(request):
    current_user = request.user
    profile=Profile.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = NewProfileForm()

    return render(request,'edit.html',{"form": form})

def like(request, image_id):
    post = Image.objects.get(id=image_id)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return redirect(details,post.id)
def details(request,image_id):
    post = Image.objects.get(id=image_id)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    return render(request,'detail.html',{"is_liked":is_liked,"post":post})

 
   
