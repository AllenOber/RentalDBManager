# Generated by Django 4.2.5 on 2023-09-26 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AquaManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegulatorDetails',
            new_name='RegulatorDetail',
        ),
        migrations.RenameModel(
            old_name='RentalOrderDetails',
            new_name='RentalOrderDetail',
        ),
        migrations.RenameModel(
            old_name='WorkOrders',
            new_name='WorkOrder',
        ),
    ]
