from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . models import Client


@login_required
def client_list(request):
    clients = Client.objects.filter(created_by=request.user)

    return render(request, 'client/client_list.html', {'clients':clients})


@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    return render(request, 'client/client_detail.html', {'client':client})
