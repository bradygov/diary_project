# diary_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from .forms import UserRegisterForm
from .models import DiaryEntry

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('diary_entries')
    else:
        form = UserRegisterForm()
    return render(request, 'diary_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('diary_entries')
    else:
        form = AuthenticationForm()
    return render(request, 'diary_app/login.html', {'form': form})

def diary_entries(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'diary_app/diary_entries.html', {'entries': entries})

def create_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        DiaryEntry.objects.create(user=request.user, title=title, content=content)
        return redirect('diary_entries')
    return render(request, 'diary_app/create_entry.html')

def edit_entry(request, entry_id):
    entry = DiaryEntry.objects.get(id=entry_id)
    if request.method == 'POST':
        entry.title = request.POST['title']
        entry.content = request.POST['content']
        entry.save()
        return redirect('diary_entries')
    return render(request, 'diary_app/edit_entry.html', {'entry': entry})

def delete_entry(request, entry_id):
    entry = DiaryEntry.objects.get(id=entry_id)
    entry.delete()
    return redirect('diary_entries')

# diary_app/views.py
def logout_view(request):
    logout(request)
    return redirect('login')