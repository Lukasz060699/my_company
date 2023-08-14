from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import Vacation
from .forms import VacationForm, VacationModeratorForm

def getAll(request):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        context = Vacation.objects.all().order_by('dateFrom').reverse().filter(user=request.user)
    else:
        context = Vacation.objects.all().order_by('dateFrom').reverse()

    return render(request, 'vacation/list.html', {'context': context})


def addNew(request):

    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        form = VacationForm(request.POST or None)
    else:
        form = VacationModeratorForm(request.POST or None)

    template = 'vacation/add.html'
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/vacation')
    context = {"form": form}
    return render(request, template, context)


def editItem(request, pk):
    item1 = get_object_or_404(Vacation, pk=pk)

    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        form = VacationForm(request.POST or None, instance=item1)
    else:
        form = VacationModeratorForm(request.POST or None, instance=item1)

    template = 'vacation/edit.html'

    if form.is_valid():
        form.save()
        return redirect('/vacation')
    context = {"form": form}
    return render(request, template, context)


def deleteItem(request, pk):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'vacation/delete.html'
    obj = get_object_or_404(Vacation, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('/vacation')
    return render(request, template)
