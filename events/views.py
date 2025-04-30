from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Event, Participation
from .forms import EventForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # connexion automatique
            return redirect("events_list")
    else:
        form = UserCreationForm()
    return render(request, "events/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("events_list")
    else:
        form = AuthenticationForm()
    return render(request, "events/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def events_list(request):
    events = Event.objects.all()
    return render(request, "events/events_list.html", {"events": events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participation, created = Participation.objects.get_or_create(user=request.user, event=event)

    if request.method == "POST":
        participation.confirmed = not participation.confirmed  # Utiliser confirmed au lieu de is_going
        participation.save()
        return redirect('event_detail', event_id=event_id)  # Rediriger pour voir le changement

    return render(request, "events/event_detail.html", {
        "event": event, 
        "participation": participation
    })

@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect("events_list")
    else:
        form = EventForm()
    return render(request, "events/create_event.html", {"form": form})
