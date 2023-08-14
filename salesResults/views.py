from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.expressions import F, Window
from django.db.models.functions.window import RowNumber

from .models import SalesResults
from .forms import SalesResultsForm

def getAll(request):
    myScore = 0
    qs = (User.objects
          .annotate(total=Count('salesresults'))
          .order_by('total')
          .annotate(rank=Window(expression=RowNumber()))).reverse()

    if User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        context = SalesResults.objects.all().order_by('date').reverse()
        #https://stackoverflow.com/questions/55260238/django-orm-create-ranking-based-on-related-model-count

        return render(request, 'salesResults/list.html', {'context': context,'countSold':qs})
    else:
        context = SalesResults.objects.all().filter(user=request.user).order_by('date').reverse()
        contextAll = SalesResults.objects.all().order_by('date').reverse()
        for x in context:
            myScore = myScore + x.price
        return render(request, 'salesResults/list.html', {'context': context, 'contextAll': contextAll, 'myScore':myScore,'countSold':qs})


def addNew(request):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'salesResults/add.html'
    form = SalesResultsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/salesresult')
    context = {"form": form}
    return render(request, template, context)


def editItem(request, pk):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'salesResults/edit.html'
    item1 = get_object_or_404(SalesResults, pk=pk)
    form = SalesResultsForm(request.POST or None, instance=item1)
    if form.is_valid():
        form.save()
        return redirect('/salesresult')
    context = {"form": form}
    return render(request, template, context)


def deleteItem(request, pk):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'salesResults/delete.html'
    obj = get_object_or_404(SalesResults, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('/salesresult')
    return render(request, template)
