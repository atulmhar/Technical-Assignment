from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Partner
from .forms import PartnerForm

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')
#     return render(request, 'login.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'partners/login.html')  # Specify the full path relative to templates


@login_required
def dashboard_view(request):
    return render(request, 'partners/dashboard.html')  # Add 'partners/' to the template path


@login_required
def partner_list_view(request):
    partners = Partner.objects.all()  # Assuming you have a Partner model
    return render(request, 'partners/partner_list.html', {'partners': partners})


@login_required
def add_partner_view(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'partners/add_partner.html', {'form': form})

@login_required
def partner_detail_view(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    return render(request, 'partners/partner_detail.html', {'partner': partner})


@login_required
def edit_partner_view(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'partners/edit_partner.html', {'form': form, 'partner': partner})
