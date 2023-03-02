from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Event
from django.views.generic import ListView, DetailView , CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.
# tjr on a du requetes


def homePage(Request):  # esm l fonction dima yabda bel miniscule
    # pour renvoyer un HTML on appel HTMLResponse
    return HttpResponse('<h1>Titlr here</h1>')


def homePage1(request):
    return render(
        request,  # 1éer param tjr request
        'events/homePage.html'  # page html à affiché
        # 3éme param .. context ( non obligatoir )
    )


def listEventsStatic(request):
    list = [
        {
            'title': 'Event 1',
            'description': 'description 1',
            'image': 'image.png'
        },
        {
            'title': 'Event 2',
            'description': 'description 2',
            'image': 'image.png'
        },
        {
            'title': 'Event 3',
            'description': 'description 3',
            'image': 'image.png'
        }
    ]
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list
        }
    )


def listEvents(request):
    list = Event.objects.all()  # objects.filter search ...
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list
        }
    )


def detailEvent(request, id):
    event = Event.objects.get(id=id)
    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
        }
    )


class listEventsViews(ListView):
    model = Event
    template_name = 'events/listEvents.html'
    context_object_name = 'events'


class EventDtails(DetailView):
    model = Event


def addEvent(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            Event.objects.create(
                **form.cleaned_data
                # Title=form.cleaned_data.get('title'),
                # Description=form.cleaned_data['Description']
            )
            return redirect('Event_ListEvent_V')
    return render(
        request,
        'events/event_add.html',
        {
            'form': form,
        }
    )


def addEventModel(request):
    form = EventModelForm()
    if request.method == 'POST':
        form = EventModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Event_ListEvent_V')
   
    return render(
        request,
        'events/event_add.html',
        {
            'form': form,
        }
    )
class EventCreateView(CreateView):
    model = Event
    form_class = EventModelForm
    success_url = reverse_lazy('Event_ListEvent_C')
    template_name ='events/event_add.html'