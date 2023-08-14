from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q


from .models import WorkSchedule
from .forms import WorkScheduleForm

def getAll(request):
    if User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        context = WorkSchedule.objects.all().order_by('dateFrom').filter(dateFrom__gte=timezone.now()).reverse()
    else:
        context = WorkSchedule.objects.all().filter(user=request.user).order_by('dateFrom').reverse()

    return render(request, 'workschedule/list.html', {'context': context})


def addNew(request):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'workschedule/add.html'
    form = WorkScheduleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/workschedule')
    context = {"form": form}
    return render(request, template, context)


def editItem(request, pk):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'workschedule/edit.html'
    item1 = get_object_or_404(WorkSchedule, pk=pk)
    form = WorkScheduleForm(request.POST or None, instance=item1)
    if form.is_valid():
        form.save()
        return redirect('/workschedule')
    context = {"form": form}
    return render(request, template, context)


def deleteItem(request, pk):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'workschedule/delete.html'
    obj = get_object_or_404(WorkSchedule, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('/workschedule')
    return render(request, template)
