from django.shortcuts import render
from django.db.models import Case, When
from django.contrib.auth.models import User
from musicbeats.models import Song
from django.contrib.auth import authenticate, login
from musicbeats.models import Watchlater

def index(request):
    song = Song.objects.all()[0:3]

    if request.user.is_authenticated:
        wl = Watchlater.objects.filter(user=request.user)
        ids = []
        for i in wl:
            ids.append(i.video_id)
        
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
        watch = Song.objects.filter(song_id__in=ids).order_by(preserved) 
        watch = reversed(watch)
    
    else:
        watch = Song.objects.all()[0:3]

    return render(request, 'index.htm', {'song': song, 'watch': watch})

def login(request):
    if request.method == "POST":
        # Check if the login form is submitted
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful, log in the user
            login(request, user)
            # Redirect to the index page after successful login
            return redirect('index')
        else:
            # Authentication failed, render the login page with an error message
            login_error = True
            return render(request, 'login.htm', {'login_error': login_error})

    # If the request method is GET, render the login page
    return render(request, 'login.htm')