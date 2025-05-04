from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import VideoForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Video, Profile
from django.core.paginator import Paginator


def home(request):
    videos = Video.objects.all()
    return render(request, 'core/home.html', {'videos': videos})



def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    
    return render(request, 'core/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
        
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()
            messages.success(request, 'Your video has been uploaded successfully!')
            return redirect('video_detail', video_id=video.id)
        else:
            messages.error(request, 'There was an error with your upload')
    else:
        form = VideoForm()

    return render(request, 'core/upload_video.html', {'form': form})

@login_required
def my_videos_list(request):
    """List all videos uploaded by the current user"""
    videos = Video.objects.filter(uploaded_by=request.user).order_by('-uploaded_at')
    return render(request, 'core/my_videos_list.html', {'videos': videos})

@login_required
def my_video_detail(request, video_id):
    """Detail view for a specific video owned by the user"""
    video = get_object_or_404(Video, id=video_id, uploaded_by=request.user)
    return render(request, 'core/my_video_detail.html', {'video': video})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # redirect to the same page after saving
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'core/profile.html', {'form': form, 'profile': profile})