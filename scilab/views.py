from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.utils import timezone
from .models import *
from .forms import *


@login_required
def equipment_list(request):
    equipment_list = Equipment.objects.all().order_by('name')
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = EquipmentsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                new_book = form.save(commit=False)
                new_book.added_by = request.user  # Assign the user to the new book
                new_book.save()  # Save the book instance
                messages.success(request, "Book added successfully!")
            except IntegrityError:
                messages.error(request, "There was an error saving the book.")
        else:
            form_errors = form.errors  # Capture form validation errors
    else:
        form = EquipmentsForm()
        
    context={      
        "form": form,
        "equipment_list": equipment_list,
        "form_errors": form_errors,}
    return render(request, 'lab/equipment_list.html', context)

@login_required
def equipment_detail(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    return render(request, 'lab/equipment_detail.html', {'equipment': equipment})

@login_required
def chemical_list(request):
    chemical_list = Chemical.objects.all().order_by('name')
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = ChemicalsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                new_book = form.save(commit=False)
                new_book.added_by = request.user  # Assign the user to the new book
                new_book.save()  # Save the book instance
                messages.success(request, "Book added successfully!")
            except IntegrityError:
                messages.error(request, "There was an error saving the book.")
        else:
            form_errors = form.errors  # Capture form validation errors
    else:
        form = ChemicalsForm()
        
    context={      
        "form": form,
        "chemical_list": chemical_list,
        "form_errors": form_errors,}
    return render(request, 'lab/chemical_list.html', context)

@login_required
def chemical_detail(request, id):
    chemical = get_object_or_404(Chemical, id=id)
    return render(request, 'lab/chemical_detail.html', {'chemical': chemical})

@login_required
def experiment_list(request):
    experiment_list = Experiment.objects.filter(researcher=request.user).order_by('-start_date')
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = ChemicalsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                new_book = form.save(commit=False)
                new_book.added_by = request.user  # Assign the user to the new book
                new_book.save()  # Save the book instance
                messages.success(request, "Book added successfully!")
            except IntegrityError:
                messages.error(request, "There was an error saving the book.")
        else:
            form_errors = form.errors  # Capture form validation errors
    else:
        form = ChemicalsForm()
        
    context={      
        "form": form,
        "chemical_list": chemical_list,
        "form_errors": form_errors,}
    return render(request, 'lab/experiment_list.html', context)

@login_required
def experiment_detail(request, id):
    experiment = get_object_or_404(Experiment, id=id)
    return render(request, 'lab/experiment_detail.html', {'experiment': experiment})

@login_required
def equipment_checkout_list(request):
    checkouts = EquipmentCheckout.objects.filter(checked_out_by=request.user).order_by('-checkout_date')
    return render(request, 'lab/checkout_list.html', {'checkouts': checkouts})

@login_required
def checkout_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    if request.method == 'POST':
        if equipment.status != 'AV':  # Ensure equipment is available
            messages.error(request, 'This equipment is not available for checkout')
            return redirect('lab:equipment_detail', id=equipment_id)
        
        checkout = EquipmentCheckout.objects.create(
            equipment=equipment,
            checked_out_by=request.user,
            expected_return_date=request.POST['expected_return_date'],
            purpose=request.POST['purpose'],
            destination=request.POST['destination'],
            condition_on_checkout=request.POST['condition_on_checkout']
        )
        messages.success(request, 'Equipment checked out successfully')
        return redirect('lab:checkout_detail', checkout_id=checkout.id)
    
    return render(request, 'lab/checkout_form.html', {'equipment': equipment})

@login_required
def return_equipment(request, checkout_id):
    checkout = get_object_or_404(EquipmentCheckout, id=checkout_id)
    if request.method == 'POST':
        checkout.actual_return_date = timezone.now()
        checkout.condition_on_return = request.POST['condition_on_return']
        checkout.status = 'RT'
        checkout.save()
        messages.success(request, 'Equipment returned successfully')
        return redirect('lab:equipment_detail', id=checkout.equipment.id)
    
    return render(request, 'lab/return_form.html', {'checkout': checkout})

@login_required
def dashboard(request):
    context = {
        'equipment_count': Equipment.objects.count(),
        'chemical_count': Chemical.objects.count(),
        'active_experiments': Experiment.objects.filter(researcher=request.user, status='IP').count(),
        'recent_experiments': Experiment.objects.filter(researcher=request.user).order_by('-start_date')[:5],
        'current_checkouts': EquipmentCheckout.objects.filter(checked_out_by=request.user, status='CO'),
        'overdue_checkouts': EquipmentCheckout.objects.filter(
            checked_out_by=request.user,
            status='CO',
            expected_return_date__lt=timezone.now()
        )
    }
    return render(request, 'lab/dashboard.html', context)
