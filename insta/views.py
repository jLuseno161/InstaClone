from insta.forms import UserProfileUpdateForm, UserprofileForm
from insta.models import Image, Profile
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    profile = Profile.objects.all()
  
    return render(request,'index.html',{"posts":posts,"profile":profile})

# @login_required(login_url='/accounts/login/')
# def newPost(request):
#     return render(request,'index.html')

@login_required(login_url='/accounts/login/')    
def insta_profile(request):
    if request.method == 'POST':
        user_profile_form = UserprofileForm(request.POST, request.FILES, instance=request.user)
        if  user_profile_form.is_valid():
            user_profile_form.save()
            return redirect('home')
    else:
        user_profile_form = UserprofileForm(instance=request.user)
        user_form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'registration/profile.html',{"user_profile_form": user_profile_form,"user_form":user_form})