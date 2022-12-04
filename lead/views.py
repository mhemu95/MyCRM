from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddLeadForm
from .models import Lead
from client.models import Client


@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user, became_client=False)
    return render(request, 'lead/leads_list.html', {'leads':leads})


def lead_detail(request, pk):
    # lead = Lead.objects.filter(created_by=request.user).get(pk=pk) or
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    return render(request, 'lead/lead_detail.html', {'lead':lead})


@login_required
def lead_update(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()

            messages.success(request, 'Lead updated successfully')

            return redirect(leads_list)
    else:
        form = AddLeadForm(instance=lead)

    return render(request, 'lead/edit_lead.html', {'form':form})


@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, 'Lead deleted.')

    return redirect(leads_list)


@login_required
def add_lead(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            messages.success(request, 'Lead created successfully')

            return redirect(leads_list)

    else:
        form = AddLeadForm()

    return render(request, 'lead/add_lead.html', {'form':form})


@login_required
def became_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    client = Client.objects.create(
        name = lead.name,
        email = lead.email,
        description = lead.description,
        created_by = request.user,
    )

    lead.became_client = True
    lead.save()

    messages.success(request, 'Lead converted to a client')

    return redirect('leads_list')
