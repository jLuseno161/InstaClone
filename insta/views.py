from django.conf import settings
from django.contrib.auth.models import User
from django.forms.widgets import DateTimeInput
from django.http.response import HttpResponse, HttpResponseRedirect
from insta.forms import CommentForm, NewPostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from insta.models import Comment, Image, Profile
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib import messages





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username, email=email,password=password)
            subject = 'welcome to GFG world'
            message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            # return HttpResponse('Please confirm your email address to complete the registration')
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()
  
    return render(request,'index.html',{"posts":posts,"profile":profile,"comment":comment})

@login_required(login_url='/accounts/login/')    
def show_profile(request):
    current_user= request.user
    images= Image.objects.filter(profile=current_user.id).all

    return render(request, 'registration/profile.html',{"images":images} )

@login_required(login_url='/accounts/login/')    
def update_profile(request,id):
    
    obj = get_object_or_404(Profile,user_id=id)
    obj2 = get_object_or_404(User,id=id)
    form = UpdateProfileForm(request.POST or None, instance = obj)
    form2 = UpdateUserForm(request.POST or None, instance = obj2)
    if form.is_valid() and form2.is_valid():
        form.save()
        form2.save()
        return HttpResponseRedirect("/profile")
    
    return render(request, "registration/update_profile.html", {"form":form, "form2":form2})

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

@login_required(login_url='/accounts/login/')
def search(request): 
    if 'profile' in request.GET and request.GET['profile']:
        user = request.GET.get("profile")

        print(user)
        results = Profile.search_profile(user)
        message = f'profile'
        return render(request, 'search.html',{'profiles': results,'message': message})
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
