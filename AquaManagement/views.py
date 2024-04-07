from django.shortcuts import render, redirect, get_object_or_404
from .models import (Customer, BCD, BCDOrderHistory, Regulator, RegulatorDetail, Wetsuit, WetsuitOrderHistory,
                     RentalOrder, RentalOrderDetail, RentalPricing, WorkOrder)
from .forms import WorkOrderForm, RentalOrderForm, BCDEquipmentForm  # <-- Import the forms here
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView



# Customer views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})


def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customer_detail.html', {'customer': customer})


# BCD views
def bcd_list(request):
    bcds = BCD.objects.all()
    return render(request, 'bcd_list.html', {'bcds': bcds})


# Rental Order views
def rental_order_list(request):
    rental_orders = RentalOrder.objects.all()
    return render(request, 'rental_order_list.html', {'rental_orders': rental_orders})


# Work Order views
def work_order_list(request):
    work_orders = WorkOrder.objects.all()
    return render(request, 'work_order_list.html', {'work_orders': work_orders})


# Rental Pricing views
def rental_pricing_list(request):
    rental_pricings = RentalPricing.objects.all()
    return render(request, 'rental_pricing_list.html', {'rental_pricings': rental_pricings})


# Create new Work Order
def new_work_order(request):
    form = WorkOrderForm()
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_order_list')
    return render(request, 'new_work_order.html', {'form': form})


# Update Work Order status
def update_work_order(request, id):
    work_order = get_object_or_404(WorkOrder, id=id)
    form = WorkOrderForm(instance=work_order)
    if request.method == 'POST':
        form = WorkOrderForm(request.POST, instance=work_order)
        if form.is_valid():
            form.save()
            return redirect('work_order_list')
    return render(request, 'update_work_order.html', {'form': form})

# Add Equipment to Rental Order
def add_equipment_to_rental_order(request, id):
    rental_order = get_object_or_404(RentalOrder, id=id)
    form = BCDEquipmentForm()
    if request.method == 'POST':
        form = BCDEquipmentForm(request.POST)
        if form.is_valid():
            bcd_equipment = form.save()  # Save the form to get the BCD object
            rental_order.bcd = bcd_equipment  # Associate the BCD with the rental_order
            rental_order.save()  # Save the updated rental_order
            return redirect('rental_order_list')
    return render(request, 'add_equipment_to_rental_order.html', {'form': form})



# Mark Equipment as Needing Replacement
def mark_equipment_for_replacement(request, id):
    bcd = get_object_or_404(BCD, id=id)
    if request.method == 'POST':
        bcd.needs_replacing = True
        bcd.save()
        return redirect('bcd_list')
    return render(request, 'mark_equipment_for_replacement.html', {'bcd': bcd})


# BCDOrderHistory Views
def bcd_order_history_list(request):
    histories = BCDOrderHistory.objects.all()
    return render(request, 'bcd_order_history_list.html', {'histories': histories})


# Regulator Views
def regulator_list(request):
    regulators = Regulator.objects.all()
    return render(request, 'regulator_list.html', {'regulators': regulators})


# RegulatorDetail Views
def regulator_detail_list(request):
    regulator_details = RegulatorDetail.objects.all()
    return render(request, 'regulator_detail_list.html', {'regulator_details': regulator_details})


# Wetsuit Views
def wetsuit_list(request):
    wetsuits = Wetsuit.objects.all()
    return render(request, 'wetsuit_list.html', {'wetsuits': wetsuits})


# WetsuitOrderHistory Views
def wetsuit_order_history_list(request):
    histories = WetsuitOrderHistory.objects.all()
    return render(request, 'wetsuit_order_history_list.html', {'histories': histories})


# RentalOrderDetail Views
def rental_order_detail_list(request):
    rental_order_details = RentalOrderDetail.objects.all()
    return render(request, 'rental_order_detail_list.html', {'rental_order_details': rental_order_details})

def new_rental_order(request):
    form = RentalOrderForm()
    if request.method == 'POST':
        form = RentalOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental_order_list')
    return render(request, 'new_rental_order.html', {'form': form})

''' Missing rental orders delete. rental orders update, and rental orders modify, including templates,
error with templates to urls. Regulator and regulator details in the models section was not configured 
correctly in django it was in mysql workbench. 

class RentalOrderDelete(DeleteView):
    model = RentalOrder
    success_url = reverse_lazy('rental_order_list')
'''
