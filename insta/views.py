from django.forms.widgets import DateTimeInput
from django.http.response import HttpResponseRedirect
from insta.forms import CommentForm, NewPostForm, ProfileForm, UpdateProfileForm
from insta.models import Comment, Image, Profile
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()
  
    return render(request,'index.html',{"posts":posts,"profile":profile,"comment":comment})

# @login_required(login_url='/accounts/login/')
# def newPost(request):
#     return render(request,'index.html')

@login_required(login_url='/accounts/login/')    
def show_profile(request):
    # if request.method == 'POST':
    #     update_form = ProfileForm(request.POST, request.FILES, instance=request.user)
    #     if  update_form.is_valid():
    #         update_form.save()
    #         return redirect('home')
    # else:
    #     update_form = ProfileForm(instance=request.user)
    #     form = UpdateProfileForm(instance=request.user)
    # return render(request, 'registration/profile.html',{"update_form":update_form,"form":form} )
    # u_profile = Profile.objects.filter(post= id)
    # images = Image.objects.filter(id=id).all()
    current_user= request.user

    images= Image.objects.filter(profile=current_user.id).all
    # post_comment = Comment.objects.filter(post= id)
    # images = Profile.objects.filter(user=current_user)

    return render(request, 'registration/profile.html',{"images":images} )



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

def search(request): 
    if 'profile' in request.GET and request.GET['profile']:
        user = request.GET.get("profile")
        results = Profile.search_profile(user)
        message = f'user'
        return render(request, 'search.html',{'results': results,'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'search.html', {'message': message})

@login_required(login_url='/accounts/login/')
def comment(request,id):
    post_comment = Comment.objects.filter(post= id)
    images = Image.objects.filter(id=id).all()
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    image = get_object_or_404(Image, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = image
            comment.user = profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()

    return render(request,'comment.html',{"form":form,"images":images,"comments":post_comment})
