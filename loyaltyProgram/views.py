from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q, F
from django.contrib import messages

from .models import LoylalityProgram, UserProfile
from .forms import LoylalityProgramForms

def getAll(request):
    if User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        context = LoylalityProgram.objects.all().order_by('date').reverse()
    else:
        #https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query
        context = LoylalityProgram.objects.all().filter(Q(user=request.user) | Q(user=None)).order_by('date').reverse()

    return render(request, 'loyalityProgram/list.html', {'context': context})


def addNew(request):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'loyalityProgram/add.html'
    form = LoylalityProgramForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/loyalityprogram')
    context = {"form": form}
    return render(request, template, context)


def getItem(request, pk):
    item1 = get_object_or_404(LoylalityProgram, pk=pk)
    if request.user.userprofile.balance - item1.price >= 0:
        item1.user = request.user
        item1.save()
        UserProfile.objects.filter(user=request.user).update(balance=F('balance') - item1.price)

    else:
        messages.add_message(request, messages.INFO, 'Masz za mało punktów')
    return redirect('/loyalityprogram')


def deleteItem(request, pk):
    if not User.objects.filter(pk=request.user.id, groups__name='moderatorzy').exists():
        return redirect('/')

    template = 'loyalityProgram/delete.html'
    obj = get_object_or_404(LoylalityProgram, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('/loyalityprogram')
    return render(request, template)
