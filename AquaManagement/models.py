# Create your models here.
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)


class BCD(models.Model):
    identifier = models.CharField(max_length=50, unique=True)
    size = models.CharField(max_length=20)
    manufacturer_model = models.CharField(max_length=100, blank=True, null=True)


class BCDOrderHistory(models.Model):
    bcd = models.ForeignKey(BCD, on_delete=models.CASCADE)
    rental_date = models.DateField()
    age_of_bcd = models.IntegerField(blank=True, null=True)
    needs_replacing = models.BooleanField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)


class Regulator(models.Model):
    set_name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    needs_replacing = models.BooleanField(default=False)


class RegulatorDetail(models.Model):
    PART_TYPE_CHOICES = [
        ('First Stage', 'First Stage'),
        ('Second Stage', 'Second Stage'),
        ('Third Stage', 'Third Stage')
    ]
    inventory = models.ForeignKey(Regulator, on_delete=models.CASCADE)
    part_type = models.CharField(max_length=20, choices=PART_TYPE_CHOICES, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    serial = models.BigIntegerField(blank=True, null=True)


class Wetsuit(models.Model):
    identifier = models.CharField(max_length=50, unique=True)
    size = models.CharField(max_length=20)
    manufacturer_model = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=10, null=True, blank=True)


# WetsuitOrderHistory
class WetsuitOrderHistory(models.Model):
    wetsuit = models.ForeignKey(Wetsuit, on_delete=models.CASCADE)
    rental_date = models.DateField()
    age_of_wetsuit = models.IntegerField(null=True, blank=True)
    needs_replacing = models.BooleanField(null=True, blank=True)


class RentalOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bcd = models.ForeignKey(BCD, on_delete=models.SET_NULL, blank=True, null=True)
    regulator = models.ForeignKey(Regulator, on_delete=models.SET_NULL, blank=True, null=True)
    wetsuit = models.ForeignKey(Wetsuit, on_delete=models.SET_NULL, blank=True, null=True)  # Added line
    rental_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    rental_status = models.CharField(max_length=50, blank=True, null=True)

    # RentalOrderDetails


class RentalOrderDetail(models.Model):
    rental_order = models.ForeignKey(RentalOrder, on_delete=models.CASCADE)
    equipment_type = models.CharField(max_length=50, null=True, blank=True)
    equipment_id = models.CharField(max_length=255, null=True, blank=True)


class RentalPricing(models.Model):
    equipment_type = models.CharField(max_length=50, blank=True, null=True)
    rental_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_scheme = models.TextField(blank=True, null=True)


# WorkOrder
class WorkOrder(models.Model):
    received_date = models.DateField(null=True, blank=True)
    target_date = models.DateField(null=True, blank=True)
    pickup_date = models.DateField(null=True, blank=True)
    issue = models.CharField(max_length=100, null=True, blank=True)
    actions_taken = models.TextField(null=True, blank=True)
    regulator = models.ForeignKey(Regulator, on_delete=models.SET_NULL, null=True, blank=True)
