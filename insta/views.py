from insta.forms import NewPostForm, ProfileForm, UpdateProfileForm
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
def show_profile(request):
    if request.method == 'POST':
        update_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if  update_form.is_valid():
            update_form.save()
            return redirect('home')
    else:
        update_form = ProfileForm(instance=request.user)
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'registration/profile.html',{"update_form":update_form,"form":form} )

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.cleaned_data.get('image')
            caption=form.cleaned_data.get('caption')
            post = Image(image = image,caption= caption, profile=profile)
            post.save()
            
        else:
            print(form.errors)

        return redirect('index')
    else:
        form = NewPostForm()

    return render(request, 'new_post.html', {"form": form})
