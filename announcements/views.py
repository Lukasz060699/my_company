from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import Announcements
from .forms import AnnouncementsForm


def index(request):
    context = Announcements.objects.all().order_by('date').reverse()
    return render(request, 'announcements/index.html', {'context': context})

def getAll(request):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    context = Announcements.objects.all().order_by('date').reverse()
    return render(request, 'announcements/list.html', {'context': context})


def addNew(request):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'announcements/add.html'
    form = AnnouncementsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/announcements')
    context = {"form": form}
    return render(request, template, context)


def editItem(request, pk):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'announcements/edit.html'
    item1 = get_object_or_404(Announcements, pk=pk)
    form = AnnouncementsForm(request.POST or None, instance=item1)
    if form.is_valid():
        form.save()
        return redirect('/announcements')
    context = {"form": form}
    return render(request, template, context)


def deleteItem(request, pk):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'announcements/delete.html'
    obj = get_object_or_404(Announcements, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('/announcements')
    return render(request, template)
