from insta.models import Image, Profile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    profile = Profile.objects.all()
  
    return render(request,'index.html',{"posts":posts,"profile":profile})
@login_required(login_url='/accounts/login/')
def newPost(request):
    return render(request,'index.html')
    