from django.urls import path
from . import views

urlpatterns = [
    path('customer_list/', views.customer_list, name='customer_list'),
    path('customer_detail/<int:id>/', views.customer_detail, name='customer_detail'),
    path('bcd_list/', views.bcd_list, name='bcd_list'),
    path('rental_order_list/', views.rental_order_list, name='rental_order_list'),
    path('work_order_list/', views.work_order_list, name='work_order_list'),
    path('rental_pricing_list/', views.rental_pricing_list, name='rental_pricing_list'),
    path('new_work_order/', views.new_work_order, name='new_work_order'),
    path('update_work_order/<int:id>/', views.update_work_order, name='update_work_order'),
    path('add_equipment_to_rental_order/<int:id>/', views.add_equipment_to_rental_order,
         name='add_equipment_to_rental_order'),
    path('mark_equipment_for_replacement/<int:id>/', views.mark_equipment_for_replacement,
         name='mark_equipment_for_replacement'),
    path('bcd_order_history_list/', views.bcd_order_history_list, name='bcd_order_history_list'),
    path('regulator_list/', views.regulator_list, name='regulator_list'),
    path('regulator_detail_list/', views.regulator_detail_list, name='regulator_detail_list'),
    path('wetsuit_list/', views.wetsuit_list, name='wetsuit_list'),
    path('wetsuit_order_history_list/', views.wetsuit_order_history_list, name='wetsuit_order_history_list'),
    path('rental_order_detail_list/', views.rental_order_detail_list, name='rental_order_detail_list'),
    path('new_rental_order/', views.new_rental_order, name='new_rental_order'),

]
